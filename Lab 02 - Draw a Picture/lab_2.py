# Import the "arcade" library
import arcade

# Open up a window.
arcade.open_window(800, 600, "TENNIS COURT")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the grass - 'left', 'right', 'top', 'bottom', and 'color'
arcade.draw_lrtb_rectangle_filled(0, 800, 800, 0, arcade.color.GO_GREEN)

# --- Draw the tennis court --- ('center_x', 'center_y', 'width', 'height', and 'color')

# First Rectangle - 'left', 'right', 'top', 'bottom', and 'color'
arcade.draw_lrtb_rectangle_filled(30, 770, 570, 30, arcade.color.BONE)

# Second Rectangle - 'left', 'right', 'top', 'bottom', and 'color'
arcade.draw_lrtb_rectangle_filled(40, 760, 560, 40, arcade.color.GO_GREEN)

# Horizontal Lines - 'center_x', 'center_y', 'width', 'height', and 'color'
arcade.draw_rectangle_filled(390, 300, 300, 10, arcade.color.BONE)
arcade.draw_rectangle_filled(400, 510, 730, 10, arcade.color.BONE)
arcade.draw_rectangle_filled(400, 100, 730, 10, arcade.color.BONE)

arcade.draw_rectangle_filled(60, 300, 45, 10, arcade.color.BONE)
arcade.draw_rectangle_filled(740, 300, 45, 10, arcade.color.BONE)

# Vertical Lines - 'center_x', 'center_y', 'width', 'height', and 'color'
arcade.draw_rectangle_filled(400, 100, 10, 1200, arcade.color.BONE)
arcade.draw_rectangle_filled(400, 20, 10, 170, arcade.color.BLACK)
arcade.draw_rectangle_filled(400, 590, 10, 170, arcade.color.BLACK)

arcade.draw_rectangle_filled(240, 300, 10, 410, arcade.color.BONE)
arcade.draw_rectangle_filled(540, 300, 10, 410, arcade.color.BONE)

# Ball - 'center_x', 'center_y', 'radius', and 'color'
arcade.draw_circle_filled(750, 476, 12, arcade.color.BITTER_LIME)


# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()