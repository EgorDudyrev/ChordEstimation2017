from scipy import absolute
import matplotlib.pyplot as plt


def plot_spectrogram(spectrogram):
    spectrogram = absolute(spectrogram)
    
    plt.figure(figsize=(15, 7.5))
    plt.imshow(spectrogram, origin="lower", cmap="jet",aspect="auto", interpolation="nearest")
    #plt.pcolormesh(times, frequencies, spectogram)
    plt.colorbar()
    plt.ylabel('Frequency')
    plt.xlabel('Frames')
    plt.show()
    
    
def map_chords(chords, _type='MinMaj'):
    #Create Dictionary for MIDI notes
    MIDInote = {'A': 57, 'A#': 58, 'Bb': 58, 'B': 59, 'Cb': 59,'C': 60, 'C#': 61, 'Db': 61,
         'D': 62, 'D#': 63, 'Eb': 63, 'E': 64, 'E#': 65, 'F': 65, 'F#': 66, 'Gb': 66, 
         'G': 67, 'G#': 68, 'Ab': 68}
    #Create dicitionary for chords in semitone intervals
    chType = {'N': 0, 'maj' : [0, 4, 7], 'min' : [0, 3, 7], 'maj7' : [0, 4, 7, 11],
          'min7' : [0, 3, 7, 10], '7' : [0, 4, 7, 10], 'sus4' : [0, 5, 7], 
          'sus2' : [0, 2, 7], 'maj6' : [0, 4, 7, 9], '1' : [0], '5' : [0, 7],
          'maj11' : [0, 4, 7, 11, 14, 17], '11' : [0, 4, 7, 10, 14, 17],
          'min11' : [0, 3, 7, 10, 14, 17], 'maj13' : [0, 4, 7, 11, 14, 17, 21],
          '13' : [0, 4, 7, 10, 14, 17, 21], 'min13' : [0, 3, 7, 10, 14, 17, 21],
          'dim' : [0, 3, 6], 'aug' : [0, 4, 8], 'min6' : [0, 3, 7, 9],
          '9' : [0, 4, 7, 10, 14], 'maj9' : [0, 4, 7, 11, 14], 'min9' : [0, 3, 7, 10, 14],
          'hdim7' : [0, 3, 6, 10], '' : [0], 'minmaj7': [0, 3, 7, 11],
          'dim7' : [0, 3, 6, 9]}
    #Intervalos a intervalos en semitonos
    interval = {'1' : 0, '2' : 2, '3' : 4, '4' : 5, '5' : 7, '6' : 9, '7' : 11,
            '8' : 12, '9' : 14, '10' : 16, '11' : 17, '12' : 19, '13' : 21}
    modifier = {'b' : -1, '#': 1}
    
    
    if type(chords)==str:
        chords = [chords]
    nchords = []
    for chord in chords:
        if len(chord) == 1:
            nchords.append('N')
            continue
        root,chord = chord.split(':')
        allowed_chords = {}
        if 'MinMaj' in _type:
            allowed_chords['maj']= chType['maj']
            allowed_chords['min']= chType['min']
        
        similar_chords = sorted([sim_ch for sim_ch in chType if chord.startswith(sim_ch)], key=lambda x: -len(x))
        if not similar_chords:
            nchords.append('Not found')
            continue 
         
        #print similar_chords
        notes = chType.get(similar_chords[0])
        if notes==0:
            nchords.append('N')
            continue
        #print 'notes',notes
        
        is_find = False
        for chName, chNotes in allowed_chords.items():
            if all([x in notes for x in chNotes]):
                nchords.append(root+':'+chName)
                is_find = True
                break
        if not is_find:
            nchords.append('N')
    return nchords