// src/components/Layout.jsx
import React from "react";
import { motion } from "framer-motion";

const Layout = ({ children }) => {
  return (
    <motion.div
      className="custom-scrollbar min-h-screen w-full bg-gradient-to-br from-slate-950 via-gray-900 to-black 
      text-white flex flex-col overflow-y-auto select-none"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.6 }}
    >
      {/* Navbar */}
      <nav className="border-b border-gray-800 px-6 py-4 flex justify-between items-center bg-gray-900/70 backdrop-blur-md sticky top-0 z-10">
        {/* Left - Logo */}
        <h1 className="text-lg font-bold bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-transparent">
          MultiGuard
        </h1>

        {/* Right - Links */}
        <div className="space-x-6 text-sm flex items-center">
          <a
            href="https://k1rbyd.github.io/MultiGuard/"
            className="text-gray-300 hover:text-white transition-colors"
          >
            Home
          </a>
          <span className="text-gray-500 cursor-default">Image Detector</span>
        </div>
      </nav>

      {/* Main Content */}
      <main className="flex-grow flex flex-col items-center justify-start w-full">
        {children}
      </main>

      {/* Footer */}
      <footer className="text-center text-xs text-gray-700 py-3 border-t border-gray-800">
        <p className="text-center text-xs text-gray-600">
          AI may occasionally be incorrect. Verify from reliable sources.
        </p>
        © {new Date().getFullYear()} MultiGuard | Image Tampering Detector
      </footer>
    </motion.div>
  );
};

export default Layout;
