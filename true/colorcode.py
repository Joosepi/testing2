        # toggle color tracking with the key bind
        key = cv2.waitKey(1) & 0xFF
        if key == ord(self.key_bind):
            self.tracking_enabled = not self.tracking_enabled
            if self.tracking_enabled:
                self.timer.start(30)
            else:
                self.timer.stop()

        # exit the program if the "Esc" key is pressed
        if key == 27:
            sys.exit()

    def set_color_range(self, lower_color, upper_color):
        self.lower_color = np.array(lower_color)
        self.upper_color = np.array(upper_color)

    def set_key_bind(self, key_bind):
        self.key_bind = key_bind

    def __del__(self):
        # release the camera and destroy all windows
        self.camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    color_tracker = ColorTracker()
