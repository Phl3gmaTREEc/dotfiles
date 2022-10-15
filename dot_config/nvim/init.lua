-- init file for NVIM config

require('ptcnvim/options')
require('ptcnvim/keymaps')
require('ptcnvim/plugins')
require('ptcnvim/nvim-tree')
require('ptcnvim/bufferline')
require('ptcnvim/treesitter')
require('ptcnvim/lualine')

vim.cmd[[colorscheme dracula]]
