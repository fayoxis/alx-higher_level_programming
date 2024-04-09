#!/usr/bin/node
charPrint(c) {
  if (typeof c === 'undefined') {
    this.print();
  } else {
    for (let i = 0; i < this.height; i++) {
      console.log(c.toString().repeat(this.width));
    }
  }
}
