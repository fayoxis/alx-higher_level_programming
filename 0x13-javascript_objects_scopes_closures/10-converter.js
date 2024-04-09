#!/usr/bin/env node

module.exports = {
  converter: (base) => (num) => num.toString(base),
};
