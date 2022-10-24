def solution(melody, k):
    answer = []

    note_map = {
        "C": 0,
        "C#": 1,
        "D": 2,
        "D#": 3,
        "E" : 4,
        "F": 5,
        "F#": 6,
        "G": 7,
        "G#": 8,
        "A": 9,
        "A#": 10,
        "B": 11

    }

    num_map = list(note_map.keys())

    min_note_num, max_note_num = 0, 83

    # 각 음에 대해 키를 수정해준다
    for note in melody:
        if len(note) == 3:
            note, octave = note[0] + note[2], note[1]
        else:
            note, octave = note[0], note[1]

        note_num = note_map[note] + 12*int(octave)
        note_num += k

        new_octave = note_num // 12
        new_note = note_num % 12

        new_note = num_map[new_note]
        new_octave = str(new_octave)
        result = ""
        if int(new_octave) < 0 or int(new_octave) > 7:
            if int(new_octave) < 0:
                result = "C0"
            else:
                result = "B7"

        else:
            if len(new_note) > 1:
                result = new_note[0] + new_octave + new_note[1]
            else:
                result = new_note + new_octave
        answer.append(result)  
    return answer

