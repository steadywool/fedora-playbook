require('telescope').setup {
    extensions = {
        file_browser = {
            hijack_netrw = true,
            hidden = true,
        },
    },
}

require('telescope').load_extension 'file_browser'
