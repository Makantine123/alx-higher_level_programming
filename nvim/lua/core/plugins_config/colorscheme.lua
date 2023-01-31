require("dracula")



function ColorVanish()

  local dracula = require("dracula")
  if (dracula.setup.colors.bg == "nil") then
    dracula.setup({
      colors = {
        innerbg = "#282A36",
      }
    })
  else
    dracula.setup({
      colors = {
        innerbg = "nil",
      }
    })
  end
end
