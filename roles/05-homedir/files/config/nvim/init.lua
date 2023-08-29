-- Leader key
vim.g.mapleader = ';'

-- Appearance
vim.cmd('colorscheme habamax')
vim.opt.termguicolors = true

-- Clipboard/Mouse
vim.opt.clipboard = 'unnamedplus'
vim.opt.mouse = 'a'

-- Search
vim.opt.ignorecase = true
vim.opt.smartcase = true

-- Files
vim.opt.undofile = true

-- Lines
vim.opt.number = true
vim.opt.cursorline = true

-- Indentation
vim.opt.autoindent = true
vim.opt.smartindent = true
vim.opt.wrap = false

-- Tabs & spaces
vim.opt.expandtab = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4

-- Disable
vim.g.loaded_python3_provider = 0
vim.g.loaded_ruby_provider = 0
vim.g.loaded_node_provider = 0
vim.g.loaded_perl_provider = 0

-- Go to next/previous buffer in buffer list
vim.keymap.set('n', '<TAB>', '<cmd>bnext<CR>')
vim.keymap.set('n', '<S-TAB>', '<cmd>bprevious<CR>')
