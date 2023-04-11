#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w <= 0 || h <= 0) {
        // Create an empty object if w or h is not a positive integer
        return {};
      }
      // Initialize width and height instance attributes with values of w and h
      this.width = w;
      this.height = h;
    }
  }
  module.exports = Rectangle;
  