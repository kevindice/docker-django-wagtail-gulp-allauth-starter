var gulp = require('gulp'),
    sass = require('gulp-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    cssnano = require('gulp-cssnano'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
    plumber = require('gulp-plumber'),
    pixrem = require('gulp-pixrem'),
    runSequence = require('run-sequence');

var env = process.env.env;
var dev = (env === "dev");

var paths = {
    out: {
        css: '/static/css',
        js: '/static/js'
    },
    in: {
        foundationSass: '/src/bower_components/foundation-sites/scss',
        motionUISass: '/src/bower_components/motion-ui/src',
        customSass: '/src/scss/custom',
        scss: '/src/scss',
        js: '/src/js'
    }
};

////////////////////////////////
//Tasks//
////////////////////////////////

// Styles autoprefixing and minification
gulp.task('styles', function () {
    var x = gulp.src(paths.in.scss + '/project.scss')
        .pipe(sass({
            includePaths: [
                paths.in.sassFoundation,
                paths.in.sassMotionUI,
                paths.in.sassCustom
            ]
        }).on('error', sass.logError))
        .pipe(plumber()) // Checks for errors
        .pipe(autoprefixer({browsers: ['last 2 version']})) // Adds vendor prefixes
        .pipe(pixrem());  // add fallbacks for rem units

    // only output unminified if in dev environment
    if (dev) {
        x.pipe(gulp.dest(paths.out.css));
    }

    x.pipe(rename({suffix: '.min'}))
        .pipe(cssnano()) // Minifies the result
        .pipe(gulp.dest(paths.out.css));
});

// Javascript minification
gulp.task('scripts', function() {
  return gulp.src(paths.out.js + '/project.js')
    .pipe(plumber()) // Checks for errors
    .pipe(uglify()) // Minifies the js
    .pipe(rename({ suffix: '.min' }))
    .pipe(gulp.dest(paths.out.js));
});

gulp.task('default', function () {
    runSequence(['styles', 'scripts']);
});

gulp.task('watch', ['default'], function(){
    gulp.watch(paths.in.scss + '/*.scss', ['styles']);
    gulp.watch(paths.in.js + '/*.js', ['scripts']);
});