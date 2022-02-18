# Big Score
# Demonstrates displaying text on a graphics screen

from ;ivewires import games, color

game.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

score = games.Text(value = 17123,
                   size = 60,
                   color = color.black,
                   x = 550,
                   y = 30)
games.screen.add(score)
game.screen.mainloop()
