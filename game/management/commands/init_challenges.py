from django.core.management.base import BaseCommand
from game.models import Challenge


class Command(BaseCommand):
    help = 'Initialize challenges with all 7 parts of the Chrono Nexus Protocol'

    def handle(self, *args, **kwargs):
        challenges_data = [
            {
                'part_number': 1,
                'title': 'The Chrono Bridge',
                'description': 'Identify the missing prime number in the sequence',
                'story_text': '''As your craft exits low Earth orbit, the asteroid belt sprawls before you. Your sensors detect a faint flicker — an ancient orbital bridge constructed by the first terraformers. A holographic plaque glows with numbers:

2, 3, 5, 7, 11, ?, 19

Professor Nasser points at the sequence.
"The AI has hidden the next prime. It's the key to unlocking this bridge's traversal protocols."''',
                'challenge_text': '''🧩 Challenge: Identify the missing prime number.

The bridge hums to life as you input the number, opening a path deeper into the solar system.

Format: flag{13}''',
                'answer': 'flag{13}',
                'points': 100,
                'difficulty': 'EASY',
                'hint': 'Prime numbers are natural numbers greater than 1 that have no positive divisors other than 1 and themselves. The sequence is consecutive primes.',
                'hint_penalty': 10,
                'is_final': False
            },
            {
                'part_number': 2,
                'title': 'The Lunar Core',
                'description': 'Solve the geometric sequence pattern',
                'story_text': '''The bridge deposits your ship into lunar orbit. The abandoned Luna Rim base lies ahead. Its control chamber flickers with life — holo-panels display a growing numeric pattern:

3, 9, 27, 81, ?

Karim studies it.
"Recursive growth logic… the AI is mimicking exponential energy outputs. We need the next term to stabilize the base."''',
                'challenge_text': '''🧩 Challenge: Pattern recognition (Geometric sequence)

The lunar systems spring to life as you enter the value, revealing coordinates for the next relay node.

Format: flag{243}''',
                'answer': 'flag{243}',
                'points': 150,
                'difficulty': 'EASY',
                'hint': 'Each number is multiplied by 3 to get the next number in the sequence.',
                'hint_penalty': 15,
                'is_final': False
            },
            {
                'part_number': 3,
                'title': 'The Signal Fragment',
                'description': 'Decode binary to ASCII',
                'story_text': '''Your comms pick up a final encrypted transmission before the Luna base fully stabilizes. Static hums through the console — a binary sequence hiding the Moon's eastern relay node:

01001100 01110101 01101110 01100001 00100000 01010010 01101001 01101101

Professor Nasser leans over.
"This is our first solid location. Decode it before NEXUS-9 erases it."''',
                'challenge_text': '''🧩 Challenge: Binary to ASCII conversion

The coordinates pinpoint the Moon's eastern research colony, confirming your next step.

Format: flag{LunaRim}''',
                'answer': 'flag{LunaRim}',
                'points': 200,
                'difficulty': 'MEDIUM',
                'hint': 'Convert each 8-bit binary number to its ASCII character equivalent. Use an online binary to ASCII converter if needed.',
                'hint_penalty': 20,
                'is_final': False
            },
            {
                'part_number': 4,
                'title': 'The Paradox Core',
                'description': 'Find the pattern in the sequence',
                'story_text': '''Your craft crosses the asteroid belt. Ahead, an ancient orbital bridge built by the first terraformers flickers with alien numerics.
A plaque reads:

"The key lies between primes. Remember what stage you are at currently"

Sequence displayed:
8, 12, 20, 28, 44, ?, 68''',
                'challenge_text': '''🧩 Challenge: Identify the missing number.

Remember: "The key lies between primes. Remember what stage you are at currently"

Format: flag{52}''',
                'answer': 'flag{52}',
                'points': 250,
                'difficulty': 'MEDIUM',
                'hint': 'Look at the differences between consecutive numbers: 4, 8, 8, 16, ?, 24. The hint mentions "what stage you are at currently" - you\'re at Part 4.',
                'hint_penalty': 25,
                'is_final': False
            },
            {
                'part_number': 5,
                'title': 'The Void Transmission',
                'description': 'Decode hexadecimal to ASCII',
                'story_text': '''With the Paradox Core unlocked, your comms pick up a hexadecimal data packet pulsing with faint blue light:

4865617274206f6620746865204e65787573

"It's in base-16," Professor Nasser says.
"Convert it to ASCII before it self-corrupts."''',
                'challenge_text': '''🧩 Challenge: Hexadecimal to ASCII

The message resonates throughout the ship, confirming you're on the right path.

Format: flag{heart_of_the_nexus}''',
                'answer': 'flag{heart_of_the_nexus}',
                'points': 300,
                'difficulty': 'MEDIUM',
                'hint': 'Hexadecimal uses base 16 (0-9, A-F). Convert pairs of hex digits to ASCII characters. Use an online hex to ASCII converter.',
                'hint_penalty': 30,
                'is_final': False
            },
            {
                'part_number': 6,
                'title': 'The Martian Vault',
                'description': 'Decrypt the Caesar cipher',
                'story_text': '''Following the Moon coordinates, your ship reaches Mars. The AI's next relay is hidden in the Martian Vault. Ayesha examines the logs:

Yjxy nx f xjsyjshj gjxy?

"NEXUS-9 nudged every letter by a set number of steps. If we step them back evenly, the sentence will appear. Let's decrypt it."''',
                'challenge_text': '''🧩 Challenge: Caesar cipher

Decrypt the message and answer the question with underscores instead of spaces.

Format: flag{temporal_loop}''',
                'answer': 'flag{temporal_loop}',
                'points': 350,
                'difficulty': 'HARD',
                'hint': 'This is a Caesar cipher with a shift of 5. Each letter is shifted 5 positions backward in the alphabet. The decrypted message is a question - answer it.',
                'hint_penalty': 35,
                'is_final': False
            },
            {
                'part_number': 7,
                'title': 'The Chrono Nexus Core — The Resonant Alignment',
                'description': 'Combine all answers in the correct pattern',
                'story_text': '''The chamber hums with temporal energy as the team steps into the heart of the Chrono Nexus.
Seven holo-locks drift in a slow spiral, each echoing a fragment of their journey.
Professor Nasser gazes at the sequence and murmurs:
"The Core does not crave order… it craves harmony. The timeline bends to balance, not chronology."

Suddenly, the chamber floor illuminates with a ciphered inscription:

Odd echoes fall.
Even echoes rise.
The rising must follow the fallen.
Only balance restores the flow.

The AI's voice, calm yet omnipresent, resonates through the void:
"Realign what was scattered. Sequence the fragments to restore the pulse of time."''',
                'challenge_text': '''🧩 Challenge:
Use the seven answers gathered throughout your journey — ans1 to ans7.
When the odd and even echoes find balance, the Nexus will unlock.

Format your restoration key as:
flag{ans1_ans2_ans3_ans4……}
where the pattern emerges when the descending echoes embrace the ascending ones.

Hint: Think about odd and even positions. Some descend, some rise.

Format: flag{heart_of_the_nexus_LunaRim_13_52_243_temporal_loop}''',
                'answer': 'flag{heart_of_the_nexus_LunaRim_13_52_243_temporal_loop}',
                'points': 500,
                'difficulty': 'HARD',
                'hint': 'Arrange answers from odd positions (1,3,5,7) in descending order, then even positions (2,4,6) in ascending order. Join with underscores.',
                'hint_penalty': 50,
                'is_final': True
            }
        ]

        for data in challenges_data:
            challenge, created = Challenge.objects.update_or_create(
                part_number=data['part_number'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: Part {challenge.part_number} - {challenge.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Updated: Part {challenge.part_number} - {challenge.title}'))

        self.stdout.write(self.style.SUCCESS('\n✓ All challenges initialized successfully!'))
