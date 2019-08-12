import csv
import time
import keyboard_listener as listener
import screenshot_taker as screenshot

image_path = "./screenshots"
output_filename = './data/recording.csv'
frames_per_second = 5


def direction_to_onehot(input):
    if input == 'Key.up+Key.left' or input == 'Key.left+Key.up':
        return 1
    elif input == 'Key.up':
        return 2
    elif input == 'Key.up+Key.right' or input == 'Key.right+Key.up':
        return 3
    elif input == 'Key.left':
        return 4
    elif input == 'Key.right':
        return 5
    elif input == 'Key.down+Key.left' or input == 'Key.left+Key.down':
        return 6
    elif input == 'Key.down':
        return 7
    elif input == 'Key.down+Key.right' or input == 'Key.right+Key.down':
        return 8
    else:
        return 0


def start_recorder():
    print('App Started')
    with open(output_filename, 'a', newline='\n') as recording_file:
        writer = csv.writer(recording_file)
        while listener.has_started:
            while listener.is_listening:
                filename = screenshot.save_screenshot(image_path)
                writer.writerow([filename, direction_to_onehot(listener.get_current_keys())])

                time.sleep(1 / frames_per_second)

    recording_file.close()


listener.setup_keyboard_listening()
start_recorder()
