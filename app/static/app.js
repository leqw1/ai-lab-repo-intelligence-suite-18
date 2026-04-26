async function loadBoard() {
  const [agents, projects, risks] = await Promise.all([
    fetch('/api/agents').then((response) => response.json()),
    fetch('/api/projects').then((response) => response.json()),
    fetch('/api/risks').then((response) => response.json()),
  ]);
  const board = document.querySelector('#board');
  board.innerHTML = [
    tile('Agents', agents.agents.map((agent) => agent.role).join('<br>')),
    tile('Projects', projects.projects.map((project) => `${project.name}: ${project.stage}`).join('<br>')),
    tile('Risk', `score: ${risks.risks.score}<br>${risks.risks.warnings.join('<br>') || 'no warnings'}`),
  ].join('');
}

function tile(title, body) {
  return `<article class="tile"><h2>${title}</h2><p>${body}</p></article>`;
}

loadBoard();
