module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy('assets');
  eleventyConfig.addPassthroughCopy({'_config/CNAME': 'CNAME'});
  return {
    passthroughFileCopy: true,
    dir: {
      input: "views",
      includes: '../_includes',
      output: "docs"
    }
  }
}