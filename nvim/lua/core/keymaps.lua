vim.g.mapleader = ' '
vim.g.maplocalleader= ' '

vim.opt.backspace = '2'
vim.opt.showcmd = true
vim.opt.laststatus = 2
vim.opt.shiftwidth = 2
vim.opt.shiftround = true
vim.opt.expandtab = true

vim.opt.number = true
vim.opt.relativenumber = false

vim.keymap.set('n', '<leader>h', ':nohlsearch<CR>')

vim.cmd[[colorscheme dracula]]
