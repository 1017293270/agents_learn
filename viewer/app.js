const state = {
  manifest: null,
  notes: [],
  selectedSection: "all",
  selectedTag: "all",
  selectedStatus: "all",
  query: "",
  activeNoteId: null
};

const els = {
  searchInput: document.querySelector("#searchInput"),
  sectionList: document.querySelector("#sectionList"),
  tagList: document.querySelector("#tagList"),
  noteList: document.querySelector("#noteList"),
  noteCount: document.querySelector("#noteCount"),
  sectionCount: document.querySelector("#sectionCount"),
  currentFilter: document.querySelector("#currentFilter"),
  readerEmpty: document.querySelector("#readerEmpty"),
  readerLoading: document.querySelector("#readerLoading"),
  readerError: document.querySelector("#readerError"),
  readerErrorText: document.querySelector("#readerErrorText"),
  readerContent: document.querySelector("#readerContent"),
  readerSection: document.querySelector("#readerSection"),
  readerTitle: document.querySelector("#readerTitle"),
  readerMeta: document.querySelector("#readerMeta"),
  markdownBody: document.querySelector("#markdownBody")
};

init();

async function init() {
  bindEvents();
  setReaderState("loading");

  try {
    const response = await fetch("./manifest.json");
    if (!response.ok) throw new Error(`manifest ${response.status}`);
    state.manifest = await response.json();
    state.notes = await Promise.all(state.manifest.notes.map(loadNote));
    state.activeNoteId = state.notes[0]?.id ?? null;
    renderNavigation();
    render();
    if (state.activeNoteId) selectNote(state.activeNoteId);
    else setReaderState("empty");
  } catch (error) {
    setReaderState("error", "manifest.json 读取失败，请确认本地服务从项目根目录启动。");
  }
}

function bindEvents() {
  els.searchInput.addEventListener("input", event => {
    state.query = event.target.value.trim().toLowerCase();
    render();
  });

  document.querySelectorAll(".state-button").forEach(button => {
    button.addEventListener("click", () => {
      document.querySelectorAll(".state-button").forEach(item => item.classList.remove("is-active"));
      button.classList.add("is-active");
      state.selectedStatus = button.dataset.status;
      render();
    });
  });
}

async function loadNote(note) {
  try {
    const response = await fetch(encodeURI(note.path));
    if (!response.ok) throw new Error(`${response.status}`);
    const markdown = await response.text();
    const parsed = parseFrontmatter(markdown);
    return {
      ...note,
      markdown,
      body: parsed.body,
      meta: {
        ...parsed.meta,
        title: parsed.meta.title || note.title,
        tags: parsed.meta.tags?.length ? parsed.meta.tags : note.tags || []
      },
      status: parsed.meta.status || "draft",
      confidence: parsed.meta.confidence || "unknown",
      depth: parsed.meta.depth || "standard"
    };
  } catch (error) {
    return {
      ...note,
      markdown: "",
      body: "",
      meta: { title: note.title, tags: note.tags || [] },
      status: "unverified",
      confidence: "unknown",
      depth: "capture",
      loadError: error.message
    };
  }
}

function parseFrontmatter(markdown) {
  if (!markdown.startsWith("---")) return { meta: {}, body: markdown };
  const end = markdown.indexOf("\n---", 3);
  if (end === -1) return { meta: {}, body: markdown };

  const raw = markdown.slice(3, end).trim();
  const body = markdown.slice(end + 4).trim();
  const meta = {};
  let currentKey = null;

  raw.split(/\r?\n/).forEach(line => {
    const keyValue = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    if (keyValue) {
      currentKey = keyValue[1];
      const value = keyValue[2].trim();
      meta[currentKey] = parseYamlValue(value);
      return;
    }

    if (currentKey && Array.isArray(meta[currentKey])) {
      const listItem = line.match(/^\s*-\s*(.*)$/);
      if (listItem && listItem[1]) meta[currentKey].push(stripQuotes(listItem[1]));
    }
  });

  return { meta, body };
}

function parseYamlValue(value) {
  if (!value) return "";
  if (value === "[]") return [];
  if (value.startsWith("[") && value.endsWith("]")) {
    return value
      .slice(1, -1)
      .split(",")
      .map(item => stripQuotes(item.trim()))
      .filter(Boolean);
  }
  return stripQuotes(value);
}

function stripQuotes(value) {
  return value.replace(/^["']|["']$/g, "");
}

function renderNavigation() {
  const sections = [{ id: "all", title: "全部模块" }, ...state.manifest.sections];

  els.sectionList.innerHTML = sections.map(section => {
    const count = section.id === "all"
      ? state.notes.length
      : state.notes.filter(note => note.section === section.id).length;
    return `<button class="section-chip${section.id === state.selectedSection ? " is-active" : ""}" data-section="${escapeHtml(section.id)}" type="button">${escapeHtml(section.title)} · ${count}</button>`;
  }).join("");

  els.sectionList.querySelectorAll("button").forEach(button => {
    button.addEventListener("click", () => {
      state.selectedSection = button.dataset.section;
      renderNavigation();
      render();
    });
  });

  renderTags();
}

function renderTags() {
  const tags = [...new Set(state.notes.flatMap(note => note.meta.tags || note.tags || []))].sort();
  els.tagList.innerHTML = [`<button class="filter-chip${state.selectedTag === "all" ? " is-active" : ""}" data-tag="all" type="button">全部</button>`]
    .concat(tags.map(tag => `<button class="filter-chip${state.selectedTag === tag ? " is-active" : ""}" data-tag="${escapeHtml(tag)}" type="button">${escapeHtml(tag)}</button>`))
    .join("");

  els.tagList.querySelectorAll("button").forEach(button => {
    button.addEventListener("click", () => {
      state.selectedTag = button.dataset.tag;
      renderTags();
      render();
    });
  });
}

function render() {
  const filtered = getFilteredNotes();
  els.noteCount.textContent = `${filtered.length} 篇`;
  els.sectionCount.textContent = `${state.manifest.sections.length} 模块`;
  els.currentFilter.textContent = currentFilterLabel();

  if (!filtered.length) {
    els.noteList.innerHTML = `<div class="empty-list">没有匹配的笔记。</div>`;
    return;
  }

  els.noteList.innerHTML = filtered.map(note => renderNoteCard(note)).join("");
  els.noteList.querySelectorAll(".note-card").forEach(button => {
    button.addEventListener("click", () => selectNote(button.dataset.noteId));
  });
}

function getFilteredNotes() {
  return state.notes.filter(note => {
    const sectionMatch = state.selectedSection === "all" || note.section === state.selectedSection;
    const tagMatch = state.selectedTag === "all" || (note.meta.tags || []).includes(state.selectedTag);
    const statusMatch = state.selectedStatus === "all" || note.status === state.selectedStatus;
    const haystack = [
      note.meta.title,
      note.title,
      note.body,
      note.section,
      ...(note.meta.tags || [])
    ].join(" ").toLowerCase();
    const queryMatch = !state.query || haystack.includes(state.query);
    return sectionMatch && tagMatch && statusMatch && queryMatch;
  });
}

function renderNoteCard(note) {
  const section = sectionTitle(note.section);
  const tags = (note.meta.tags || []).slice(0, 4).map(tag => `<span>${escapeHtml(tag)}</span>`).join("");
  const active = note.id === state.activeNoteId ? " is-active" : "";
  return `
    <button class="note-card${active}" data-note-id="${escapeHtml(note.id)}" type="button">
      <p>${escapeHtml(section)}</p>
      <h3>${escapeHtml(note.meta.title || note.title)}</h3>
      <p>${escapeHtml(note.status)} · ${escapeHtml(note.depth)} · ${escapeHtml(note.confidence)}</p>
      <div class="note-card-tags">${tags}</div>
    </button>
  `;
}

function selectNote(noteId) {
  const note = state.notes.find(item => item.id === noteId);
  if (!note) return;

  state.activeNoteId = noteId;
  render();

  if (note.loadError) {
    setReaderState("error", `${note.title} 读取失败：${note.loadError}`);
    return;
  }

  els.readerSection.textContent = sectionTitle(note.section);
  els.readerTitle.textContent = note.meta.title || note.title;
  els.readerMeta.innerHTML = [
    note.status,
    note.depth,
    note.confidence,
    ...(note.meta.tags || [])
  ].map(item => `<span class="meta-pill">${escapeHtml(item)}</span>`).join("");
  els.markdownBody.innerHTML = renderMarkdown(note.body);
  setReaderState("content");
}

function setReaderState(mode, message = "") {
  els.readerEmpty.hidden = mode !== "empty";
  els.readerLoading.hidden = mode !== "loading";
  els.readerError.hidden = mode !== "error";
  els.readerContent.hidden = mode !== "content";
  els.readerErrorText.textContent = message;
}

function currentFilterLabel() {
  const parts = [];
  if (state.selectedSection !== "all") parts.push(sectionTitle(state.selectedSection));
  if (state.selectedTag !== "all") parts.push(`#${state.selectedTag}`);
  if (state.selectedStatus !== "all") parts.push(state.selectedStatus);
  if (state.query) parts.push(`"${state.query}"`);
  return parts.length ? parts.join(" / ") : "全部";
}

function sectionTitle(sectionId) {
  return state.manifest.sections.find(section => section.id === sectionId)?.title || sectionId;
}

function renderMarkdown(markdown) {
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  let html = "";
  let i = 0;
  let inList = false;
  let inOrderedList = false;

  const closeLists = () => {
    if (inList) {
      html += "</ul>";
      inList = false;
    }
    if (inOrderedList) {
      html += "</ol>";
      inOrderedList = false;
    }
  };

  while (i < lines.length) {
    const line = lines[i];

    if (line.startsWith("```")) {
      closeLists();
      const lang = line.slice(3).trim();
      i += 1;
      const code = [];
      while (i < lines.length && !lines[i].startsWith("```")) {
        code.push(lines[i]);
        i += 1;
      }
      html += `<pre><code data-lang="${escapeHtml(lang)}">${escapeHtml(code.join("\n"))}</code></pre>`;
      i += 1;
      continue;
    }

    if (isTableStart(lines, i)) {
      closeLists();
      const tableLines = [];
      while (i < lines.length && /^\|.*\|$/.test(lines[i].trim())) {
        tableLines.push(lines[i]);
        i += 1;
      }
      html += renderTable(tableLines);
      continue;
    }

    const trimmed = line.trim();
    if (!trimmed) {
      closeLists();
      i += 1;
      continue;
    }

    const heading = trimmed.match(/^(#{1,3})\s+(.*)$/);
    if (heading) {
      closeLists();
      const level = heading[1].length;
      html += `<h${level}>${renderInline(heading[2])}</h${level}>`;
      i += 1;
      continue;
    }

    const bullet = trimmed.match(/^-\s+(.*)$/);
    if (bullet) {
      if (inOrderedList) {
        html += "</ol>";
        inOrderedList = false;
      }
      if (!inList) {
        html += "<ul>";
        inList = true;
      }
      html += `<li>${renderInline(bullet[1])}</li>`;
      i += 1;
      continue;
    }

    const ordered = trimmed.match(/^\d+\.\s+(.*)$/);
    if (ordered) {
      if (inList) {
        html += "</ul>";
        inList = false;
      }
      if (!inOrderedList) {
        html += "<ol>";
        inOrderedList = true;
      }
      html += `<li>${renderInline(ordered[1])}</li>`;
      i += 1;
      continue;
    }

    closeLists();
    html += `<p>${renderInline(trimmed)}</p>`;
    i += 1;
  }

  closeLists();
  return html;
}

function isTableStart(lines, index) {
  return /^\|.*\|$/.test(lines[index]?.trim() || "") &&
    /^\|\s*[-:]+\s*(\|\s*[-:]+\s*)+\|$/.test(lines[index + 1]?.trim() || "");
}

function renderTable(lines) {
  const [header, , ...rows] = lines;
  const headers = splitTableRow(header);
  const bodyRows = rows.map(splitTableRow);
  return `
    <table>
      <thead><tr>${headers.map(cell => `<th>${renderInline(cell)}</th>`).join("")}</tr></thead>
      <tbody>${bodyRows.map(row => `<tr>${row.map(cell => `<td>${renderInline(cell)}</td>`).join("")}</tr>`).join("")}</tbody>
    </table>
  `;
}

function splitTableRow(line) {
  return line.trim().replace(/^\||\|$/g, "").split("|").map(cell => cell.trim());
}

function renderInline(text) {
  let output = escapeHtml(text);
  output = output.replace(/`([^`]+)`/g, "<code>$1</code>");
  output = output.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noreferrer">$1</a>');
  return output;
}

function escapeHtml(value = "") {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
