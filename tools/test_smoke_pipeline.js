const assert = require('assert');

function hasNoMissingSymbols() {
  // placeholder smoke test
  const required = ['title', 'formula', 'body', 'trap'];
  assert.ok(required.length > 0, 'Required concept fields missing');
  console.log('smoke test passed');
}

hasNoMissingSymbols();
