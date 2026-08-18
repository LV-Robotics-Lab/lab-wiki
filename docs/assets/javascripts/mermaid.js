mermaid.initialize({ startOnLoad: false });

document$.subscribe(async () => {
  await mermaid.run({
    nodes: document.querySelectorAll(".mermaid"),
  });
});
