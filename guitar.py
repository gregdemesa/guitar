from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

# Define a keyboard mapping
keyboard = "q2we4r5ty7u8i9op-[=]"

# Create a list of GuitarString objects, one for each note on the keyboard
guitarStrings = []
for i in range(len(keyboard)):
    frequency = 440 * 1.059463 ** (i - 12)
    guitarStrings.append(GuitarString(frequency))

    # Create a set to store the plucked strings
    pluckedStrings = set()

    # Initialize the window
    stdkeys.create_window()
    n_iters = 0
# Main loop
while True:

    # Check if it's time to poll for key events
    if n_iters == 1000:
        stdkeys.poll()
        n_iters = 0

    n_iters += 1

    # Check if the user has typed a key
    if stdkeys.has_next_key_typed():

        # Get the key that the user typed
        key = stdkeys.next_key_typed()

        # Check if the key is in the keyboard mapping
        if key in keyboard:

            # Get the index of the corresponding note
            index = keyboard.index(key)

            # Pluck the string if the key is 'q' and the index is 0, or if the key is any other key and the index is not 0
            if key == 'q' and index == 0:
                guitarStrings[index].pluck()
                pluckedStrings.add(guitarStrings[index])
            elif index != 0:
                guitarStrings[index].pluck()
                pluckedStrings.add(guitarStrings[index])

    # Compute the superposition of samples
    samples = []
    for note in pluckedStrings:
        samples.append(note.sample())
    sample = sum(samples)

    # Play the sample
    play_sample(sample)

    # Advance the simulation of each guitar string by one step
    for note in guitarStrings:
        note.tick()