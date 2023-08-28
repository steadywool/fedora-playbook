" Enable filetype plugins
filetype plugin on
filetype indent on

" Leader key
let mapleader = ";"

" Appearance
syntax enable
colorscheme habamax
set showmatch

" Clipboard/Mouse
set clipboard=unnamedplus
set mouse=a

" Search
set wildmenu
set ignorecase
set smartcase

" Files
set nobackup
set noswapfile
set undofile

" Line number
set number
set cursorline

" Indentation
set autoindent
set smartindent
set nowrap

" Use spaces instead of tabs
set expandtab
set smarttab
set tabstop=4
set shiftwidth=4

" Go to next/previous buffer in buffer list
nnoremap <TAB> :bnext<CR>
nnoremap <S-TAB> :bprevious<CR>
