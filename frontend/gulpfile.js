var gulp = require('gulp'),
    sass = require('gulp-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    cssnano = require('gulp-cssnano'),
    uglify = require('gulp-uglify'),
    _ = require('lodash');

var paths = {
    out: {
        css: '/static/css',
        js: '/static/js'
    },
    in: {
        foundationSass: '/src/bower_components/foundation-sites/scss',
        motionUISass: '/src/bower_components/motion-ui/src',
        customSass: '/src/sass/custom',
        scss: '/src/scss',
        js: '/src/js'
    }
};

gulp.task('default', function() {

});