// what: Defines a function greet that logs "hello" to the console.
// why: Provides a reusable greeting for demos or scripts.
// reads_writes: No inputs; writes "hello" to stdout via console.
// contracts: Caller invokes greet(); no arguments; logs "hello".
// risks: None for local use; avoid in sensitive logging contexts.

function greet(): void {
  console.log("hello");
}

greet();
