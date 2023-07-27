import re
def myers_briggs():
    pattern = r'^[a-zA-Z ]+$'
    name = input("What is your name: \n")
    valid_name = bool(re.match(pattern,name))
    if not valid_name:
        while True:
            name = input("(Invalid name (symbol(s) or number(s) make the name invalid))What is your name: \n")
            valid_name = bool(re.match(pattern, name))
            if valid_name:
                break
    if valid_name:
        questions = [
            ["A. Expend energy, enjoy groups", "B. Conserve energy, one-on-one"],
            ["A. Interpret literally", "B. Look for meaning and possibilities"],
            ["A. Logical, thinking, questioning.", "B. Empathetic, feeling, accommodating"],
            ["A. Organized, orderly.", "B. Flexible, adaptable"],
            ["A. More outgoing, think out loud.", "B. More reserved, think to yourself."],
            ["A. Practical, realistic, experiential.", "B. Imagination, innovative, theoretical."],
            ["A. Candid, straight forward, frank.", "B. Tactful, kind, encouraging."],
            ["A. Plan, schedule.", "B. Unplanned, spontaneous"],
            ["A. seek many tasks, public activities, interaction with others","B. seek private, solitary activities with quiet to concentrate."],
            ["A. standard, usual, conventional. ", "B. different, novel, unique."],
            ["A. firm, tend to criticize, hold the line.", "B. gentle, tend to appreciate, conciliate."],
            ["A.regulated, structured.", "B. easygoing, live  and let live"],
            ["A. external, communicative, express yourself.", "B. internal, reticent, keep to yourself."],
            ["A. focus on here-and-now.", "B. look to the future, global perspective, \"big picture\""],
            ["A. tough minded, just.", "B. tender-hearted, merciful"],
            ["A. preparation, plan ahead.", "B. go with the flow, adapt as you go."],
            ["A. active, initiate.", "B. reflective, deliberate"],
            ["A. facts, things, \"what is\"", "B. ideas, dreams, \"what could be\", philosophical"],
            ["A. matter of fact, issue oriented", "B. sensitive, people-oriented, compassionate"],
            ["A. control, govern", "B. latitude, freedom"]
             ]

        answers = [0 for _ in range(20)]
        count_i = 0
        count_e = 0
        count_s = 0
        count_n = 0
        count_t = 0
        count_f = 0
        count_j = 0
        count_p = 0
        index = 0
        while index < len(questions):
            print(questions[index][0],'\t',questions[index][1])
            answer = input()
            if answer.capitalize() in ['B', 'A']:
                if index % 4 == 0:
                    match answer.capitalize():
                        case 'A':
                            answers[index] = questions[index][0]
                            count_e += 1
                        case 'B':
                            answers[index] = questions[index][1]
                            count_i += 1
                elif index % 4 == 1:
                    match answer.capitalize():
                        case 'A':
                            answers[index] = questions[index][0]
                            count_s += 1
                        case 'B':
                            answers[index] = questions[index][1]
                            count_n += 1
                elif index % 4 == 2:
                    match answer.capitalize():
                        case 'A':
                            answers[index] = questions[index][0]
                            count_t += 1
                        case 'B':
                            answers[index] = questions[index][1]
                            count_f += 1
                elif index % 4 == 3:
                    match answer.capitalize():
                        case 'A':
                            answers[index] = questions[index][0]
                            count_j += 1
                        case 'B':
                            answers[index] = questions[index][1]
                            count_p += 1
                index +=1
        type_indicator = '' + ('E' if count_e > count_i else 'I')
        type_indicator += 'S' if count_s > count_n else 'N'
        type_indicator += 'T' if count_t > count_f else 'F'
        type_indicator += 'J' if count_j > count_p else 'P'
        print(f'Hello {name} you selected: ')
        for answer in answers[::4]:
            print(answer)
        print(f'Number of A selected: {count_e}')
        print(f'Number of B selected: {count_i}')
        print()
        for answer in answers[1::4]:
            print(answer)
        print(f'Number of A selected: {count_s}')
        print(f'Number of B selected: {count_n}')
        print()
        for answer in answers[2::4]:
            print(answer)
        print(f'Number of A selected: {count_t}')
        print(f'Number of B selected: {count_f}')
        print()
        for answer in answers[3::4]:
            print(answer)
        print(f'Number of A selected: {count_j}')
        print(f'Number of B selected: {count_p}')
        match type_indicator:
            case 'ENFJ':
                print("""
                ENFJ personalites
                
                A ENFJ is a person with the Extraverted, Intuitive, Feeling, and Judging personality traits.
                These warm, forthright types love helping others, and they tend to have strong ideas and values.
                They back their perspective with the creative energy to achieve their goals.
                
                ENFJs feel called to serve a greater purpose in life. Thoughtful and idealistic,
                these personality types strive to have a positive impact on other people and the world around them.
                They rarely shy away from an opportunity to do the right thing, even when doing so is far from easy.
                                        
                ENFJs are born leaders, which explains why these personalities can be found among many notable politicians,
                coaches, and teachers. Their passion and charisma allow them to inspire others not just in their careers
                but in every arena of their lives, including their relationships. Few things bring ENFJs a deeper sense of joy and
                fulfillment than guiding friends and loved ones to grow into their best selves.
                                        
                ENFJs tend to be vocal about their values, including authenticity and altruism. When something strikes them as unjust or wrong,
                they speak up. But they rarely come across as brash or pushy, as their sensitivity and insight guide them to speak in ways that resonate with others.
                                        
                People with this personality type are devoted altruists, ready to face slings and arrows in order to stand up for the people and
                ideas that they believe in. This strength of conviction bolsters ENFJs’ innate leadership skills, particularly their ability to
                guide people to work together in service of the greater good.""")
            case 'ENFP':
                print("""
                ENFP
                A ENFP (ENFP) is someone with the Extraverted, Intuitive, Feeling, and Prospecting personality traits.
                These people tend to embrace big ideas and actions that reflect their sense of hope and goodwill toward others.
                Their vibrant energy can flow in many directions.
                                        
                It doesn’t interest me what you do for a living. I want to know what you ache for – and
                if you dare to dream of meeting your heart’s longing.
                                        
                ENFPs (ENFPs) are true free spirits – outgoing, openhearted, and open-minded. With their lively, upbeat approach to life,
                they stand out in any crowd. But even though they can be the life of the party, ENFPs don’t just care about having a good time.
                These personality types run deep – as does their longing for meaningful, emotional connections with other people.
                                        
                Friendly and outgoing, ENFPs are devoted to enriching their relationships and their social lives. But beneath their sociable,
                easygoing exteriors, they have rich, vibrant inner lives as well. Without a healthy dose of imagination, creativity, and curiosity,
                a ENFP simply wouldn’t be a ENFP.
                                        
                In their unique way, ENFPs can be quite introspective. They can’t help but ponder the deeper meaning and significance of life – even when
                they should be paying attention to something else. These personalities believe that everything – and everyone – is connected, and they live
                for the glimmers of insight that they can gain into these connections.
                                        
                ENFPs are independent and creative, always on the lookout for the magic and meaning in everyday life.
                When something sparks their imagination, ENFPs can show an enthusiasm that is nothing short of infectious.
                These personalities radiate a positive energy that draws in other people, and ENFPs may find themselves being held
                up by their peers as a leader or guru. But once the initial bloom of inspiration wears off, ENFPs can struggle with
                self-discipline and consistency, losing steam on projects that once meant so much to them.
                                        
                Seeking Joy
                ENFPs are proof that seeking out life’s joys and pleasures isn’t the same as being shallow. Seemingly in the blink of an eye,
                people with this personality type can transform from impassioned idealists to carefree figures on the dance floor.
                                        
                ENFP personalities are capable of intense thought and feeling – and also of kicking back and having a good time.
                Even in moments of fun, ENFPs want to connect emotionally with others. Few things matter more to these personality types
                than having genuine, heartfelt conversations with the people they cherish. ENFPs believe that everyone deserves to express their feelings,
                and their empathy and warmth create spaces where even the most timid spirits can feel comfortable opening up.""")
            case 'ENTJ':
                print("""
                ENTJ personalities
                A (ENTJ) is someone with the Extraverted, Intuitive, Thinking, and Judging personality traits. They are decisive people who love momentum and accomplishment.
                They gather information to construct their creative visions but rarely hesitate for long before acting on them.\s
                If there’s anything ENTJs love,it’s a good challenge, big or small, and they firmly believe that given enough time and resources, they can achieve
                any goal. This quality makes people with the Commander personality type brilliant entrepreneurs, and their ability to think strategically and hold a long-term focus
                while executing each step of their plans with determination and precision makes them powerful business leaders.
                                        
                 ENTJs see inefficiency not just as a problem in its own right, but as something that pulls time and energy away from all their future goals, an elaborate
                 sabotage consisting of irrationality and laziness. People with the Commander personality type will root out such behavior wherever they go.
                Energetic – Rather than finding this process taxing Commanders are energized by it, genuinely enjoying leading their teams forward as they implement their plans and goals.
                ENTJ couldn’t do this if they were plagued by self-doubt – they trust their abilities, make known their opinions, and believe in their capacities as leaders.
                Strong-Willed – Nor do they give up when the going gets tough – Commander personalities strive to achieve their goals, but really nothing is quite as
                satisfying to them as rising to the challenge of each obstacle in their run to the finish line.
                ENTJ exemplify the difference between moment-to-moment crisis management and navigating the challenges and steps of a bigger plan, and are known for examining
                every angle of a problem and not just resolving momentary issues, but moving the whole project forward with their solutions. These qualities combine to create
                individuals who are able to inspire and invigorate others, who people actually want to be their leaders, and this in turn helps Commanders to accomplish their often
                ambitious goals that could never be finished alone.
                """)
            case 'ENTP':
                print("""
                ENTP personalities
                                        
                An (ENTP) is a person with the Extraverted, Intuitive, Thinking, and Prospecting personality traits. They tend to be bold and creative, deconstructing and
                rebuilding ideas with great mental agility. They pursue their goals vigorously despite any resistance they might encounter.
                Quick-witted and audacious, ENTP aren’t afraid to disagree with the status quo. In fact, they’re not afraid to disagree with pretty much anything or anyone.
                Few things light up people with this personality type more than a bit of verbal sparring – and if the conversation veers into controversial terrain, so much the better.
                                        
                ENTP are known for their rebellious streak. For this personality type, no belief is too sacred to be questioned, no idea is too fundamental to be scrutinized,
                and no rule is too important to be broken, or at least thoroughly tested. Sometimes ENTP even rebel against their own beliefs by arguing the opposing viewpoint – just to
                see how the world looks from the other side.
                some of the weakness of the ENTP are that they have mental exercise of debating and to them, nothing is sacred. They often misjudge others feelings and push their debtates well
                past others tolerance level. sometimes this personalities find it difficult to focus.
                some of the Strength of this personality is that hey are very knowledgeable, they are quick thinkers, and excellent brainstormers. Their confidence, quick
                thought and ability to connect disparate ideas in novel ways create a style of communication that is charming, even entertaining, and informative at the same time.
                """)
            case 'ISFP':
                print("""
                An ISFP (ISFP) is a person with the Introverted, Observant, Feeling, and Prospecting personality traits. They tend to have open minds, approaching life,
                new experiences, and people with grounded warmth. Their ability to stay in the moment helps them uncover exciting potentials.
                                        
                I change during the course of a day. I wake and I’m one person, and when I go to sleep I know for certain I’m somebody else.
                                        
                BOB DYLAN
                ISFPs are true artists – although not necessarily in the conventional sense. For this personality type, life itself is a canvas for self-expression.
                From what they wear to how they spend their free time, ISFPs act in ways that vividly reflect who they are as unique individuals.
                                        
                And every ISFP is certainly unique. Driven by curiosity and eager to try new things, people with this personality often have a fascinating array of passions and interests.
                With their exploratory spirits and their ability to find joy in everyday life, ISFPs can be among the most interesting people you’ll ever meet. The only irony? Unassuming and
                humble, ISFPs tend to see themselves as “just doing their own thing,” so they may not even realize how remarkable they really are.
                                        
                                        
                The Beauty of an Open Mind
                ISFPs embrace a flexible, adaptable approach to life. Some personality types thrive on strict schedules and routines – but not ISFPs. ISFPs take each day as it comes, doing
                what feels right to them in the moment. And they make sure to leave plenty of room in their lives for the unexpected – with the result that many of their most cherished memories
                are of spontaneous, spur-of-the-moment outings and adventures, whether by themselves or with their loved ones.
                                        
                This flexible mindset makes ISFPs remarkably tolerant and open-minded. These personalities genuinely love living in a world filled with all kinds of people – even people who disagree
                with them or choose radically different lifestyles. It’s no surprise, then, that ISFPs are unusually open to changing their minds and rethinking their opinions. If any personality
                type believes in giving something (or someone) a second chance, it’s ISFPs.
                                        
                ISFPs want to live in a world where they – and everyone else – have the freedom to live as they see fit, without judgment.
                That said, ISFPs’ go-with-the-flow mentality can have its downsides. People with this personality type may struggle to set long-term plans – let alone stick with them. As a result,
                ISFPs tend to have a pretty cloudy view of their ability to achieve their goals, and they often worry about letting other people down. ISFPs may find that adding a little structure to
                their lives goes a long way toward helping them feel more capable and organized – without quashing their independent spirits.
                                        
                Living in Harmony
                In their relationships, ISFPs are warm, friendly, and caring, taking wholehearted enjoyment in the company of their nearest and dearest. But make no mistake: this is an Introverted personality
                type, meaning that ISFPs need dedicated alone time to recharge their energy after socializing with others. This alone time is what allows ISFPs to reestablish a sense of their own identity – in other
                words, to reconnect with who they truly are.
                """)
            case 'ESTP':
                print("""
                An ESTP\s
                ESTP is someone with the Extraverted, Observant, Thinking, and Prospecting personality traits. They tend to be energetic and action-oriented, deftly navigating whatever is in front of them. They love
                uncovering life’s opportunities, whether socializing with others or in more personal pursuits.
                                        
                ESTPs always have an impact on their immediate surroundings – the best way to spot them at a party is to look for the whirling eddy of people flitting about them as they move from group to group. Laughing
                and entertaining with a blunt and earthy humor, ESTP personalities love to be the center of attention. If an audience member is asked to come on stage, ESTPs volunteer – or volunteer a shy friend.
                                        
                Theory, abstract concepts and plodding discussions about global issues and their implications don’t keep ESTPs interested for long. ESTPs keep their conversation energetic, with a good dose of
                intelligence, but they like to talk about what is – or better yet, to just go out and do it. ESTPs leap before they look, fixing their mistakes as they go, rather than sitting idle, preparing
                contingencies and escape clauses.
                                        
                                        
                Diving Right In
                ESTPs are the likeliest personality type to make a lifestyle of risky behavior. They live in the moment and dive into the action – they are the eye of the storm. People with the ESTP personality
                type enjoy drama, passion, and pleasure, not for emotional thrills, but because it’s so stimulating to their logical minds. They are forced to make critical decisions based on factual, immediate reality
                in a process of rapid-fire rational stimulus response.
                                        
                This makes school and other highly organized environments a challenge for ESTPs. It certainly isn’t because they aren’t smart, and they can do well, but the regimented, lecturing approach of formal
                education is just so far from the hands-on learning that ESTPs enjoy. It takes a great deal of maturity to see this process as a necessary means to an end, something that creates more exciting opportunities.
                                        
                Also challenging is that to ESTPs, it makes more sense to use their own moral compass than someone else’s. Rules were made to be broken. This is a sentiment few high school instructors or corporate
                supervisors are likely to share, and can earn ESTP personalities a certain reputation. But if they minimize the trouble-making, harness their energy, and focus through the boring stuff, ESTPs are a
                force to be reckoned with.
                                        
                The Path Less Traveled
                With perhaps the most perceptive, unfiltered view of any type, ESTPs have a unique skill in noticing small changes. Whether a shift in facial expression, a new clothing style, or a broken habit, people
                with this personality type pick up on hidden thoughts and motives where most types would be lucky to pick up anything specific at all. ESTPs use these observations immediately, calling out the change and
                asking questions, often with little regard for sensitivity. ESTPs should remember that not everyone wants their secrets and decisions broadcast.""")
            case 'ESTJ':
                print("""
                ESTJ
                                        
                An ESTJ (ESTJ) is someone with the Extraverted, Observant, Thinking, and Judging personality traits. They possess great fortitude, emphatically following their own sensible judgment. They often
                serve as a stabilizing force among others, able to offer solid direction amid adversity.
                                        
                Good order is the foundation of all things.
                                        
                EDMUND BURKE
                ESTJs are representatives of tradition and order, utilizing their understanding of what is right, wrong and socially acceptable to bring families and communities together. Embracing the values of honesty,
                dedication and dignity, people with the ESTJ personality type are valued for their clear advice and guidance, and they happily lead the way on difficult paths. Taking pride in bringing people together, ESTJs
                often take on roles as community organizers, working hard to bring everyone together in celebration of cherished local events, or in defense of the traditional values that hold families and communities together.
                                        
                ESTJ (ESTJ) personality
                Leading by Example
                Demand for such leadership is high in democratic societies, and forming no less than 11% of the population, it’s no wonder that many of America’s presidents have been ESTJs. Strong believers in the rule of law
                and authority that must be earned, ESTJ personalities lead by example, demonstrating dedication and purposeful honesty, and an utter rejection of laziness and cheating, especially in work. If anyone declares
                hard, manual work to be an excellent way to build character, it is ESTJs.
                                        
                ESTJs are aware of their surroundings and live in a world of clear, verifiable facts – the surety of their knowledge means that even against heavy resistance, they stick to their principles and push an unclouded
                vision of what is and is not acceptable. Their opinions aren’t just empty talk either, as ESTJs are more than willing to dive into the most challenging projects, improving action plans and sorting details along
                the way, making even the most complicated tasks seem easy and approachable.
                                        
                However, ESTJs don’t work alone, and they expect their reliability and work ethic to be reciprocated – people with this personality type meet their promises, and if partners or subordinates jeopardize them through
                incompetence or laziness, or worse still, dishonesty, they do not hesitate to show their wrath. This can earn them a reputation for inflexibility, a trait shared by all Sentinel personalities, but it’s not because
                ESTJs are arbitrarily stubborn, but because they truly believe that these values are what make society work.
                                        
                A Greater Responsibility
                ESTJs are classic images of the model citizen: they help their neighbors, uphold the law, and try to make sure that everyone participates in the communities and organizations they hold so dear.
                The main challenge for ESTJs is to recognize that not everyone follows the same path or contributes in the same way. A true leader recognizes the strength of the individual, as well as that of the group,
                and helps bring those individuals’ ideas to the table. That way, ESTJs really do have all the facts, and are able to lead the charge in directions that work for everyone.""")
            case'ESFJ':
                print("""
                ESFJ
                                        
                A ESFJ (ESFJ) is a person with the Extraverted, Observant, Feeling, and Judging personality traits. They are attentive and people-focused, and they enjoy taking part in their social community.
                Their achievements are guided by decisive values, and they willingly offer guidance to others.
                                        
                Encourage, lift, and strengthen one another. For the positive energy spread to one will be felt by us all.
                                        
                DEBORAH DAY
                For ESFJs, life is sweetest when it’s shared with others. People with this personality type form the bedrock of many communities, opening their homes – and their hearts – to friends, loved ones, and neighbors.
                                        
                This doesn’t mean that ESFJs like everyone, or that they’re saints. But ESFJs do believe in the power of hospitality and good manners, and they tend to feel a sense of duty to those around them.
                Generous and reliable, people with this personality type often take it upon themselves – in ways both large and small – to hold their families and their communities together.
                                        
                ESFJs have a talent for making the people in their lives feel supported, cared for, and secure.
                                        
                The Beauty of a Responsible Life
                ESFJs are altruists. They take seriously their responsibilities to give back, serve others, and do the right thing.
                                        
                And ESFJs believe that there is a clear right thing to do in nearly every situation. While some personality types adopt a more lenient, live-and-let-live attitude, ESFJs may find it difficult not
                to judge when someone takes a path that strikes them as misguided. As a result, ESFJs often struggle to accept it when someone – particularly someone they care about – disagrees with them.
                                        
                ESFJs have a clear moral compass – and it can be nothing short of baffling to them when other people’s actions don’t align with it.
                With their definite views on right and wrong, ESFJs tend to be on the opinionated side. But these opinions aren’t arbitrary – they’re often based on a deep respect for tradition. ESFJs know that
                everything they do affects someone else, and they trust that established laws, protocols, and social norms will help them navigate their everyday lives in a way that is considerate and responsible toward others.
                                        
                Building Relationships That Last
                Supportive and outgoing, ESFJs can always be spotted at a party – they’re the ones fluttering around making sure that everyone else is having a good time! But make no mistake: ESFJs don’t just breeze through
                other people’s lives. Loyal to the core, they build lasting relationships, and they can be counted on to show up whenever a helping hand – or a listening ear – is needed.
                                        
                ESFJs rarely miss a birthday or holiday. Devoted to their relationships, they commit even the smallest details of their friends’ and loved ones’ lives to memory.
                With their love of order and structure, ESFJs prefer planned events to open-ended activities or spontaneous get-togethers – and they’re happy to host in order to ensure that everything goes smoothly.
                People with this personality type put a great deal of energy into making other people feel special and celebrated, and they may take it personally when someone doesn’t seem to appreciate their efforts.
                                        
                For many people with the ESFJ personality type, one of life’s greatest challenges is accepting that they can’t control anyone else’s thoughts or behavior – not even those who are nearest and dearest to them.
                Fortunately, ESFJs can find peace and fulfillment by focusing on what they do best: setting an example of care, consideration, and responsibility – and bringing people together in the process.""")
            case 'ESFP':
                print("""
                An ESFP
                ESFP is a person with the Extraverted, Observant, Feeling, and Prospecting personality traits. These people love vibrant experiences, engaging in life eagerly and taking pleasure in discovering the unknown.
                They can be very social, often encouraging others into shared activities.
                                        
                                        
                If anyone is to be found spontaneously breaking into song and dance, it is the ESFP personality type. ESFPs get caught up in the excitement of the moment, and want everyone else to feel that way, too.
                No other personality type is as generous with their time and energy as ESFPs when it comes to encouraging others, and no other personality type does it with such irresistible style.
                                        
                Living with Passion
                ESFPs love the spotlight, and all the world’s a stage. Many famous people with the ESFP personality type are indeed actors, but they love putting on a show for their friends too, chatting with a unique
                and earthy wit, soaking up attention and making every outing feel a bit like a party. Utterly social, ESFPs enjoy the simplest things, and there’s no greater joy for them than just having fun with a good
                group of friends.
                                        
                It’s not just talk either – ESFPs have the strongest aesthetic sense of any personality type. From grooming and outfits to a well-appointed home, ESFP personalities have an eye for fashion. Knowing what’s
                attractive the moment they see it, ESFPs aren’t afraid to change their surroundings to reflect their personal style. ESFPs are naturally curious, exploring new designs and styles with ease.
                                        
                Though it may not always seem like it, ESFPs know that it’s not all about them – they are observant, and very sensitive to others’ emotions. People with this personality type are often the first to help
                someone talk out a challenging problem, happily providing emotional support and practical advice. However, if the problem is about them, ESFPs are more likely to avoid a conflict altogether than to address
                it head-on. ESFPs usually love a little drama and passion, but not so much when they are the focus of the criticisms it can bring.
                                        
                A Spontaneous Spirit
                The biggest challenge ESFPs face is that they are often so focused on immediate pleasures that they neglect the duties and responsibilities that make those luxuries possible. Complex analysis, repetitive tasks,
                and matching statistics to real consequences are not easy activities for ESFPs. They’d rather rely on luck or opportunity, or simply ask for help from their extensive circle of friends. It is important for ESFPs
                to challenge themselves to keep track of long-term things like their retirement plans or sugar intake – there won’t always be someone else around who can help to keep an eye on these things.
                                        
                ESFPs recognize value and quality, which on its own is a fine trait. In combination with their tendency to be poor planners though, this can cause them to live beyond their means, and credit cards are
                especially dangerous. More focused on leaping at opportunities than in planning out long-term goals, ESFPs may find that their inattentiveness has made some activities unaffordable.
                                        
                There’s nothing that makes ESFPs feel quite as unhappy as realizing that they are boxed in by circumstance, unable to join their friends.
                ESFPs are welcome wherever there’s a need for laughter, playfulness, and a volunteer to try something new and fun – and there’s no greater joy for ESFP personalities than to bring everyone else along for
                the ride. ESFPs can chat for hours, sometimes about anything but the topic they meant to talk about, and share their loved ones’ emotions through good times and bad. If they can just remember to keep their
                ducks in a row, they’ll always be ready to dive into all the new and exciting things the world has to offer, friends in tow.""")
            case 'ISTP':
                print("""
                 ISTP\s
                 ISTP is someone with the Introverted, Observant, Thinking, and Prospecting personality traits. They tend to have an individualistic mindset, pursuing goals without needing much external connection.
                 They engage in life with inquisitiveness and personal skill, varying their approach as needed.
                                        
                I wanted to live the life, a different life. I didn’t want to go to the same place every day and see the same people and do the same job. I wanted interesting challenges.
                                        
                HARRISON FORD
                ISTPs love to explore with their hands and their eyes, touching and examining the world around them with cool rationalism and spirited curiosity. People with this personality type are natural Makers,
                moving from project to project, building the useful and the superfluous for the fun of it, and learning from their environment as they go. Often mechanics and engineers, ISTPs find no greater joy than
                in getting their hands dirty pulling things apart and putting them back together, just a little bit better than they were before.
                                        
                                        
                ISTPs explore ideas through creating, troubleshooting, trial and error and first-hand experience. They enjoy having other people take an interest in their projects and sometimes don’t even mind them
                getting into their space. Of course, that’s on the condition that those people don’t interfere with ISTPs’ principles and freedom, and they’ll need to be open to ISTPs returning the interest in kind.
                                        
                ISTPs enjoy lending a hand and sharing their experience, especially with the people they care about, and it’s a shame they’re so uncommon, making up only about five percent of the population. ISTP women
                are especially rare, and the typical gender roles that society tends to expect can be a poor fit – they’ll often be seen as tomboys from a young age.
                                        
                Dare to Differ
                While their mechanical tendencies can make them appear simple at a glance, ISTPs are actually quite enigmatic. Friendly but very private, calm but suddenly spontaneous, extremely curious but unable to
                stay focused on formal studies, ISTP personalities can be a challenge to predict, even by their friends and loved ones. ISTPs can seem very loyal and steady for a while, but they tend to build up a store
                of impulsive energy that explodes without warning, taking their interests in bold new directions.
                                        
                Rather than some sort of vision quest though, ISTPs are merely exploring the viability of a new interest when they make these seismic shifts.
                ISTPs’ decisions stem from a sense of practical realism, and at their heart is a strong sense of direct fairness, a “do unto others” attitude, which really helps to explain many of ISTPs’ puzzling traits.
                Instead of being overly cautious though, avoiding stepping on toes in order to avoid having their toes stepped on, ISTPs are likely to go too far, accepting likewise retaliation, good or bad, as fair play.
                                        
                The biggest issue ISTPs are likely to face is that they often act too soon, taking for granted their permissive nature and assuming that others are the same. They’ll be the first to tell an insensitive joke,
                get overly involved in someone else’s project, roughhouse and play around, or suddenly change their plans because something more interesting came up.
                                        
                Defying the Rules
                ISTPs will come to learn that many other personality types have much more firmly drawn lines on rules and acceptable behavior than they do – they don’t want to hear an insensitive joke, and certainly
                wouldn’t tell one back, and they wouldn’t want to engage in horseplay, even with a willing party. If a situation is already emotionally charged, violating these boundaries can backfire tremendously.
                                        
                ISTPs have a particular difficulty in predicting emotions, but this is just a natural extension of their fairness, given how difficult it is to gauge ISTPs’ emotions and motivations. However, their tendency
                to explore their relationships through their actions rather than through empathy can lead to some very frustrating situations. People with the ISTP personality type struggle with boundaries and guidelines,
                preferring the freedom to move about and color outside the lines if they need to.
                                        
                Finding an environment where they can work with good friends who understand their style and unpredictability, combining their creativity, sense of humor and hands-on approach to build practical solutions and things,
                will give ISTPs many happy years of building useful boxes – and admiring them from the outside.""")
            case 'ISTJ':
                print("""
                ISTJ
                A Logistician (ISTJ) is someone with the Introverted, Observant, Thinking, and Judging personality traits. These people tend to be reserved yet willful, with a rational outlook on life. They compose their
                actions carefully and carry them out with methodical purpose.
                                        
                ISTJ pride themselves on their integrity. People with this personality type mean what they say, and when they commit to doing something, they make sure to follow through.
                                        
                This personality type makes up a good portion of the overall population, and while ISTJ may not be particularly flashy or attention-seeking, they do more than their share to keep society on a sturdy,
                stable foundation. In their families and their communities, ISTJ often earn respect for their reliability, their practicality, and their ability to stay grounded and logical, even in the most stressful situations.
                                        
                The core of ISTJ’ self-respect comes from a sense of personal integrity. People with this personality type believe that there is a right way to proceed in any situation – and that anyone who pretends otherwise
                is probably trying to bend the rules to suit their own purposes. ISTJ have a deep respect for structure and tradition, and they are often drawn to organizations, workplaces, and educational settings that offer
                clear hierarchies and expectations.
                                        
                For many ISTJ, a lack of structure offers not freedom, but chaos.
                People with the Logistician personality type rarely hesitate to take responsibility for their actions and choices. Generally speaking, they are quick to own up to their own mistakes, admitting the truth even
                if it doesn’t make them look good. To ISTJ, honesty is far more important than showmanship, and they’d rather satisfy their own conscience than lie to impress someone else.
                                        
                ISTJ’ dedication is an admirable quality, and it drives many of their accomplishments. But it can also become a weakness that other people take advantage of. With their strong work ethic and sense of duty, ISTJ
                may routinely find themselves shouldering other people’s responsibilities. Even if they don’t complain about the situation, ISTJ can end up exhausted or discouraged if they’re constantly expected – or taking it
                upon themselves – to pick up the slack for their colleagues, friends, or loved ones.""")
            case 'ISFJ':
                print("""
                ISFJ
                A ISFJ () is someone with the Introverted, Observant, Feeling, and Judging personality traits. These people tend to be warm and unassuming in their own steady way. They’re efficient and responsible, giving
                careful attention to practical details in their daily lives.
                                        
                Love only grows by sharing. You can only have more for yourself by giving it away to others.
                                        
                BRIAN TRACY
                In their unassuming, understated way, ISFJs help make the world go round. Hardworking and devoted, people with this personality type feel a deep sense of responsibility to those around them. ISFJs can be
                counted on to meet deadlines, remember birthdays and special occasions, uphold traditions, and shower their loved ones with gestures of care and support. But they rarely demand recognition for all that they
                do, preferring instead to operate behind the scenes.
                                        
                This is a capable, can-do personality type, with a wealth of versatile gifts. Though sensitive and caring, ISFJs also have excellent analytical abilities and an eye for detail. And despite their reserve,
                they tend to have well-developed people skills and robust social relationships. ISFJs are truly more than the sum of their parts, and their varied strengths shine in even the most ordinary aspects of their
                daily lives.
                                        
                ISFJs are true altruists, meeting kindness with kindness-in-excess and engaging with the work and people they believe in with enthusiasm and generosity.
                                        
                The Gift of Loyalty
                Among ISFJs’ most distinctive traits is loyalty. Rare is the ISFJ who allows a friendship or relationship to fade away from lack of effort. Instead, they invest a great deal of energy into maintaining
                strong connections with their loved ones – and not just by sending “How are you doing?” texts. People with this personality type are known for dropping everything and lending a hand whenever a friend or family
                member is going through a hard time.
                                        
                ISFJs tend to feel most energized and effective when they’re showing up for someone who needs their help.
                ISFJs’ sense of loyalty doesn’t stop with their nearest and dearest – it often extends to their communities, their employers, and even family traditions. But the intensity of their commitment and desire to
                serve can have its downsides. Other people may take advantage of ISFJs’ helpful, hardworking nature, leaving them feeling burned out and overworked. And ISFJs may feel guilty or stressed when they contemplate
                changes – even necessary changes – to themselves, their relationships, or the way they’ve done things in the past.
                                        
                The Highest of Standards
                For ISFJs, “good enough” is rarely good enough. People with this personality type can be meticulous to the point of perfectionism. They take their responsibilities personally, consistently going above and beyond
                and doing everything that they can to exceed others’ expectations.
                                        
                ISFJ personalities are known for their humility, and they rarely seek the spotlight.
                But what happens when ISFJs’ efforts go unnoticed or unappreciated? While ISFJs tend to underplay their accomplishments, that doesn’t mean that they don’t enjoy recognition – or that they’re fine with being taken
                for granted. Unless they learn to stand up for themselves, ISFJs may find themselves quietly losing their enthusiasm and motivation, eventually becoming resentful toward the people who just don’t seem to appreciate
                them.
                                        
                Showing Up for Others – and Themselves
                Although they’re Introverted, ISFJs have a deeply social nature. Thanks to their ability to remember the details of other people’s lives, ISFJs have a special talent for making their friends and acquaintances feel
                seen, known, and cherished. Few personality types can match ISFJs’ ability to choose just the right gift for any occasion, whether large or small.
                                        
                Dedicated and thoughtful, ISFJs find great joy in helping those around them build stable, secure, and happy lives. It may not be easy for people with this personality type to show up for themselves in the way that
                they show up for other people, but when they do, they often find themselves with even more energy and motivation to do good in the world.""")
            case 'INTJ':
                print("""
                INTJ pesonality type
                An INTJ is a person with the Introverted, Intuitive, Thinking, and Judging personality traits. These thoughtful tacticians love perfecting the details of life, applying creativity and rationality to everything
                they do. Their inner world is often a private, complex one.
                Rational and quick-witted, INTJs pride themselves on their ability to think for themselves, not to mention their uncanny knack for seeing right through phoniness and hypocrisy. But because their minds are
                never at rest, Architects may struggle to find people who can keep up with their nonstop analysis of everything around them.
                                        
                This personality type comes with a strong independent streak. INTJs don’t mind acting alone, perhaps because they don’t like waiting around for others to catch up with them. They also generally prefer making
                decisions without asking for anyone else’s input. At times, this lone-wolf behavior can come across as insensitive, as it fails to take into consideration other people’s thoughts, desires, and plans.
                                        
                Architects contemplate the strengths and weaknesses of each move before they make it. And they never lose faith that, with enough ingenuity and insight, they can find a way to win – no matter what challenges
                might arise along the way.
                                        
                INTJ personalities can be rational, informed, independent, determined curious, and original. And some are their weaknesses is that they are arogant, dismissive of  emotions, Overly Critical, Combative,
                Socially Clueless.
                """)
            case 'INTP':
                print("""
                INTP personalities
                A (INTP) is someone with the Introverted, Intuitive, Thinking, and Prospecting personality traits. These flexible thinkers enjoy taking an unconventional approach to many aspects of life.
                They often seek out unlikely paths, mixing willingness to experiment with personal creativity.
                INTP often lose themselves in thought – which isn’t necessarily a bad thing. People with this personality type hardly ever stop thinking. From the moment they wake up, their minds buzz with ideas,
                questions, and insights. At times, they may even find themselves conducting full-fledged debates in their own heads.
                People with this personality type want to understand everything in the universe, but one area in particular tends to mystify them: human nature. As their name suggests, Logicians feel most at
                home in the realm of logic and rationality. As a result, they can find themselves baffled by the illogical, irrational ways that feelings and emotions influence people’s behavior – including their own.
                                        
                Some of this personality strength is that they analyze everything that they come across, from research data to the behavior of the people around them. Thanks to their unrelenting imagination, Logicians
                can come up with creative, counterintuitive ideas that wouldn’t occur to most people. Logicians are driven by curiosity and an intense desire to learn everything that they can. These personalities are
                always casting about for new pursuits, hobbies, and areas of research. they care about the truth. Rather than taking comfort in ideology or received ideas, they want to understand what’s really going on
                beneath the surface of things.""")
            case 'INFP':
                print("""
                A  (INFP) is someone who possesses the Introverted, Intuitive, Feeling, and Prospecting personality traits. These rare personality types tend to be quiet, open-minded, and imaginative, and they apply a
                caring and creative approach to everything they do.
                                        
                Although they may seem quiet or unassuming,  (INFPs) have vibrant, passionate inner lives. Creative and imaginative, they happily lose themselves in daydreams, inventing all sorts of stories and
                conversations in their minds. These personalities are known for their sensitivity – INFP can have profound emotional responses to music, art, nature, and the people around them.
                                        
                Idealistic and empathetic, INFP long for deep, soulful relationships, and they feel called to help others. But because this personality type makes up such a small portion of the population,
                INFPs may sometimes feel lonely or invisible, adrift in a world that doesn’t seem to appreciate the traits that make them unique.
                                        
                Empathy is among this personality type’s greatest gifts, but at times it can be a liability. The troubles of the world weigh heavily on INFP’ shoulders, and these personalities can be vulnerable
                to internalizing other people’s negative moods or mindsets. Unless they learn to set boundaries, INFP may feel overwhelmed by just how many wrongs there are that need to be set right.
                                        
                People with this personality type tend to feel directionless or stuck until they connect with a sense of purpose for their lives. For many INFP, this purpose has something to do with uplifting others
                and their ability to feel other people’s suffering as if it were their own. While INFP want to help everyone, they need to focus their energy and efforts – otherwise, they can end up exhausted.""")
            case 'INFJ':
                print("""
                An Advocate (INFJ) is someone with the Introverted, Intuitive, Feeling, and Judging personality traits. They tend to approach life with deep thoughtfulness and imagination. Their inner vision,
                personal values, and a quiet, principled version of humanism guide them in all things.
                                        
                “Treat people as if they were what they ought to be and you help them to become what they are capable of being.”
                                        
                (INFJs) may be the rarest personality type of all, but they certainly leave their mark on the world. Idealistic and principled, they aren’t content to coast through life – they want to stand up
                and make a difference. For Advocate personalities, success doesn’t come from money or status but from seeking fulfillment, helping others, and being a force for good in the world.
                                        
                While they have lofty goals and ambitions, INFJs shouldn’t be mistaken for idle dreamers. People with this personality type care about integrity, and they’re rarely satisfied until they’ve done
                what they know to be right. Conscientious to the core, they move through life with a clear sense of their values, and they aim never to lose sight of what truly matters – not according to other
                people or society at large, but according to their own wisdom and intuition.
                                        
                Perhaps because their personality type is so uncommon, INFJs tend to carry around a sense – whether conscious or not – of being different from most people. With their rich inner lives and their deep,
                abiding desire to find their life purpose, they don’t always fit in with those around them. This isn’t to say that Advocates can’t enjoy social acceptance or close relationships – only that they sometimes
                feel misunderstood or at odds with the world.
                                        
                INFJ may be Introverted, but they value deep, authentic relationships with others. Few things bring these personalities as much joy as truly knowing another person – and being known in return. Advocates
                enjoy meaningful conversations far more than small talk, and they tend to communicate in a way that is warm and sensitive""")


myers_briggs()
