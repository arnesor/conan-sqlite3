[![Download](https://api.bintray.com/packages/arnesor/public-conan/sqlite3%3Aarnesor/images/download.svg) ](https://bintray.com/arnesor/public-conan/sqlite3%3Aarnesor/_latestVersion)
[![Build Status](https://travis-ci.org/arnesor/conan-sqlite3.svg?branch=stable%2F3.21.0)](https://travis-ci.org/arnesor/conan-sqlite3)
[![Build status](https://ci.appveyor.com/api/projects/status/github/arnesor/conan-sqlite3?branch=stable%2F3.21.0&svg=true)](https://ci.appveyor.com/project/arnesor/conan-sqlite3)

[Conan.io](https://conan.io) package recipe for [*sqlite3*](https://www.sqlite.org).

Self-contained, serverless, in-process SQL database engine.

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/arnesor/public-conan/sqlite3%3Aarnesor).

## For Users: Use this package

### Basic setup

    $ conan install sqlite3/3.21.0@arnesor/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    sqlite3/3.21.0@arnesor/stable

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to arnesor conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create arnesor/stable


### Available Options
See https://www.sqlite.org/compile.html for details.

| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| shared      | False |  [True, False] |
| fPIC      | True |  [True, False] |
| threadsafe      | 1 |  [0, 1, 2] |
| enable_column_metadata      | False |  [True, False] |
| enable_explain_comments      | False |  [True, False] |
| enable_fts3      | False |  [True, False] |
| enable_json1      | False |  [True, False] |
| enable_rtree      | False |  [True, False] |

## Add Remote

    $ conan remote add arnesor "https://api.bintray.com/conan/arnesor/public-conan"

## Upload

    $ conan upload sqlite3/3.21.0@arnesor/stable --all -r arnesor


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package sqlite3.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](https://github.com/arnesor/conan-sqlite3.git/blob/stable/3.21.0/LICENSE)
