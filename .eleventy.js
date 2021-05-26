module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy('assets');
  return {
    passthroughFileCopy: true,
    dir: {
      input: "views",
      includes: '../_includes'
    }
  }
}