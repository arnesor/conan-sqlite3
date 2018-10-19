#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class ConanSqlite3(ConanFile):
    name = "sqlite3"
    version = "3.21.0"
    year = "2017"
    sha1 = "ebe33c20d37a715db95288010c1009cd560f2452"
    description = "Self-contained, serverless, in-process SQL database engine."
    url = "http://github.com/bincrafters/conan-sqlite3"
    homepage = "https://www.sqlite.org"
    license = "Public Domain"
    generators = "cmake"
    settings = "os", "compiler", "arch", "build_type"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt", "FindSQLite3.cmake"]
    options = {"shared": [True, False],
               "fPIC": [True, False],
               "threadsafe": [0, 1, 2],
               "enable_column_metadata": [True, False],
               "enable_explain_comments": [True, False],
               "enable_fts3": [True, False],
               "enable_json1": [True, False],
               "enable_rtree": [True, False],
               "have_fdatasync": [True, False],
               "have_gmtime_r": [True, False],
               "have_localtime_r": [True, False],
               "have_posix_fallocate": [True, False],
               "have_strerror_r": [True, False],
               "have_usleep": [True, False]
               }
    default_options = "shared=False",\
                      "fPIC=True",\
                      "threadsafe=1",\
                      "enable_column_metadata=False",\
                      "enable_explain_comments=False",\
                      "enable_fts3=False",\
                      "enable_json1=False",\
                      "enable_rtree=False",\
                      "have_fdatasync=True",\
                      "have_gmtime_r=True",\
                      "have_localtime_r=True",\
                      "have_posix_fallocate=True",\
                      "have_strerror_r=True",\
                      "have_usleep=True"

    def source(self):
        base_url = "https://www.sqlite.org/" + self.year
        archive_name = "sqlite-amalgamation-" + self.version.replace(".","") + "000"
        archive_ext = "zip"
        download_url = "{0}/{1}.{2}".format(base_url, archive_name, archive_ext)
        self.output.info("Attempting download of sources from: " + download_url)
        tools.get(download_url, sha1=self.sha1)
        os.rename(archive_name, "sources")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        cmake = CMake(self)
        cmake.definitions["THREADSAFE"] = self.options.threadsafe
        cmake.definitions["ENABLE_COLUMN_METADATA"] = self.options.enable_column_metadata
        cmake.definitions["ENABLE_EXPLAIN_COMMENTS"] = self.options.enable_explain_comments
        cmake.definitions["ENABLE_FTS3"] = self.options.enable_fts3
        cmake.definitions["ENABLE_JSON1"] = self.options.enable_json1
        cmake.definitions["ENABLE_RTREE"] = self.options.enable_rtree
        cmake.definitions["HAVE_FDATASYNC"] = self.options.have_fdatasync
        cmake.definitions["HAVE_GMTIME_R"] = self.options.have_gmtime_r
        cmake.definitions["HAVE_LOCALTIME_R"] = self.options.have_localtime_r
        cmake.definitions["HAVE_POSIX_FALLOCATE"] = self.options.have_posix_fallocate
        cmake.definitions["HAVE_STRERROR_R"] = self.options.have_strerror_r
        cmake.definitions["HAVE_USLEEP"] = self.options.have_usleep

        if self.settings.os != "Windows":
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("FindSQLite3.cmake", ".", ".")
        self.copy("*.h", dst="include", src="sources")
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", keep_path=False)
        self.copy(pattern="*.a", dst="lib", keep_path=False)
        self.copy(pattern="*.pdb", dst="lib", keep_path=False)
        self.copy(pattern="*.so", dst="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['sqlite3']
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")
            self.cpp_info.libs.append("dl")
