def under_construction(name):
    print(f'''
    *****************************************************
                {name}
    *****************************************************
              UNDER
            CONSTRUCTION
    *****************************************************
    ''')


def home():
    print('''
    *****************************************************
                        MENU
    *****************************************************
    1.Phone book
    2.Messages
    3.Chat
    4.Call register
    5.Tones
    6.Settings
    7.Call divert
    8.Games
    9.Calculator
    10.Reminders
    11.Clock
    12.Profiles
    13.Messages
    14.Power off
    *****************************************************
        *Select a function using the number beside it*
    *****************************************************
    ''')
    function = input('Enter number: ')
    if function == '1':
        phonebook()
    elif function == '2':
        messages()
    elif function == '3':
        under_construction('Chat')
        return home()
    elif function == '4':
        def call_register():
            print('''
                    *****************************************************
                                Call register
                    *****************************************************
                    1.Missed calls
                    2.Received calls
                    3.Dialled numbers
                    4.Erase recent call lists
                    5.Show call duration
                    6.Show call costs
                    7.Call cost settings
                    8.Prepaid credit
                    9.Home
                    *****************************************************
                       *Select a function using the number beside it*
                    *****************************************************
                    ''')
            function = input('Enter number: ')
            if function == '1':
                under_construction('Missed calls')
                return call_register()
            elif function == '2':
                under_construction('Received calls')
                return call_register()
            elif function == '3':
                under_construction('Dialled numbers')
                return call_register()
            elif function == '4':
                under_construction('Erase recent call lists')
                return call_register()
            elif function == '5':
                def show_call_duration():
                    print('''
                            *****************************************************
                                        Show call duration
                            *****************************************************
                            1.Last call duration
                            2.All calls duration
                            3.Received calls duration
                            4.Dialled calls duration
                            5.Clear timers
                            6.Back
                            7.Home
                            *****************************************************
                               *Select a function using the number beside it*
                            *****************************************************
                            ''')
                    function = input('Enter number: ')
                    if function == '1':
                        under_construction('Last call duration')
                        return show_call_duration()
                    elif function == '2':
                        under_construction('All calls duration')
                        return show_call_duration()
                    elif function == '3':
                        under_construction('Received calls duration')
                        return show_call_duration()
                    elif function == '4':
                        under_construction('Dialled calls duration')
                        return show_call_duration()
                    elif function == '5':
                        under_construction('Clear timers')
                        return show_call_duration()
                    elif function == '6':
                        return call_register()
                    elif function == '7':
                        return home()
                    else:
                        return show_call_duration()
                show_call_duration()
            elif function == '6':
                def show_call_cost():
                    print('''
                            *****************************************************
                                        Show call costs
                            *****************************************************
                            1.Last call cost
                            2.All calls cost
                            3.Clear counters
                            *****************************************************
                               *Select a function using the number beside it*
                            *****************************************************
                            ''')
                    function = input('Enter number: ')
                    if function == '1':
                        under_construction('Last call cost')
                        return show_call_cost()
                    elif function == '2':
                        under_construction('All calls cost')
                        return show_call_cost()
                    elif function == '3':
                        under_construction('Clear counters')
                        return show_call_cost()
                    elif function == '4':
                        return call_register()
                    elif function == '5':
                        return home()
                    else:
                        return show_call_cost()
                show_call_cost()
            elif function == '7':
                def call_cost_settings():
                    print('''
                            *****************************************************
                                        Call cost settings
                            *****************************************************
                            1.Call cost limit
                            2.Show costs in
                            3.Back
                            4.Home
                            *****************************************************
                               *Select a function using the number beside it*
                            *****************************************************
                            ''')
                    function = input('Enter number: ')
                    if function == '1':
                        under_construction('Call cost limit')
                        return call_cost_settings()
                    elif function == '2':
                        under_construction('Show cost in')
                        return call_cost_settings()
                    elif function == '3':
                        return call_register()
                    elif function == '4':
                        return home()
                    else:
                        return call_cost_settings()
                call_cost_settings()
            elif function == '8':
                under_construction('Prepaid credit')
                return call_register()
            elif function == '9':
                return home()
            else:
                return call_register()
        call_register()
    elif function == '5':
        def tone():
            print('''
                    *****************************************************
                                Tones
                    *****************************************************
                    1.Ringing tone
                    2.Ringing volume
                    3.Incoming call alert
                    4.Composer
                    5.Message alert tone
                    6.Keypad tones
                    7.Warning and game tones
                    8.Vibrating alert
                    9.Screen saver
                    10.Home
                    *****************************************************
                       *Select a function using the number beside it*
                    *****************************************************
                    ''')
            function = input('Enter number: ')
            if function == '1':
                under_construction('Ringing tone')
                return tone()
            elif function == '2':
                under_construction('Ringing volume')
                return tone()
            elif function == '3':
                under_construction('Incoming call alert')
                return tone()
            elif function == '4':
                under_construction('Composer')
                return tone()
            elif function == '5':
                under_construction('Message alert tone')
                return tone()
            elif function == '6':
                under_construction('Keypad tones')
                return tone()
            elif function == '7':
                under_construction('Warning and game tones')
                return tone()
            elif function == '8':
                under_construction('Vibrating alert')
                return tone()
            elif function == '9':
                under_construction('Screen saver')
                return tone()
            elif function == '10':
                return home()
            else:
                return tone()
        tone()
    elif function == '6':
        def settings():
            print('''
                    *****************************************************
                                Settings
                    *****************************************************
                    1.Call settings
                    2.Phone settings
                    3.Security settings
                    4.Restore factory settings
                    5.Home
                    *****************************************************
                       *Select a function using the number beside it*
                    *****************************************************
                    ''')
            function = input('Enter number: ')
            if function == '1':
                def call_settings():
                    print('''
                            *****************************************************
                                        Call settings
                            *****************************************************
                            1.Automatic redial
                            2.Speed dialling
                            3.Call waiting options
                            4.Own number sending
                            5.Phone line in use
                            6.Automatic answer
                            7.Back
                            8.Home
                            *****************************************************
                               *Select a function using the number beside it*
                            *****************************************************
                            ''')
                    function = input('Enter number: ')
                    if function == '1':
                        under_construction('Automatic Redial')
                        return call_settings()
                    elif function == '2':
                        under_construction('Speed dialling')
                        return call_settings()
                    elif function == '3':
                        under_construction('Call waiting options')
                        return call_settings()
                    elif function == '4':
                        under_construction('Own number sending')
                        return call_settings()
                    elif function == '5':
                        under_construction('Phone line in use')
                        return call_settings()
                    elif function == '6':
                        under_construction('Automatic answer')
                        return call_settings()
                    elif function == '7':
                        return settings()
                    elif function == '8':
                        return home()
                    else:
                        return call_settings()
                call_settings()
            elif function == '2':
                def phone_settings():
                    print('''
                            *****************************************************
                                        Phone settings
                            *****************************************************
                            1.Language
                            2.Cell info display
                            3.Welcome note
                            4.Network selection
                            5.Lights
                            6.Confirm SIM service actions
                            7.Back
                            8.Home
                            *****************************************************
                               *Select a function using the number beside it*
                            *****************************************************
                            ''')
                    function = input('Enter number: ')
                    if function == '1':
                        under_construction('Language')
                        return phone_settings()
                    elif function == '2':
                        under_construction('Cell info display')
                        return phone_settings()
                    elif function == '3':
                        under_construction('Welcome note')
                        return phone_settings()
                    elif function == '4':
                        under_construction('Network selection')
                        return phone_settings()
                    elif function == '5':
                        under_construction('Lights')
                        return phone_settings()
                    elif function == '6':
                        under_construction('Confirm SIM service actions')
                        return phone_settings()
                    elif function == '7':
                        return settings()
                    elif function == '8':
                        return home()
                    else:
                        return phone_settings()
                phone_settings()
            elif function == '3':
                def security_settings():
                    print('''
                            *****************************************************
                                        Security settings
                            *****************************************************
                            1.PIN code request
                            2.Call barring service
                            3.Fixed dialling
                            4.Closed user group
                            5.Phone security
                            6.Change access codes
                            7.Back
                            8.Home
                            *****************************************************
                               *Select a function using the number beside it*
                            *****************************************************
                            ''')
                    function = input('Enter number: ')
                    if function == '1':
                        under_construction('PIN code request')
                        return security_settings()
                    elif function == '2':
                        under_construction('Call  barring service')
                        return security_settings()
                    elif function == '3':
                        under_construction('Fixed dialling')
                        return security_settings()
                    elif function == '4':
                        under_construction('Closed user group')
                        return security_settings()
                    elif function == '5':
                        under_construction('Phone security')
                        return security_settings()
                    elif function == '6':
                        under_construction('Change access codes')
                        return security_settings()
                    elif function == '7':
                        return settings()
                    elif function == '8':
                        return home()
                    else:
                        return security_settings()
                security_settings()
            elif function == '4':
                under_construction('Restore factory settings')
                return settings()
            elif function == '5':
                return home()
            else:
                return settings()
        settings()
    elif function == '7':
        under_construction('Call divert')
        return home()
    elif function == '8':
        under_construction('Games')
        return home()
    elif function == '9':
        under_construction('Calculator')
        return home()
    elif function == '10':
        under_construction('Reminders')
        return home()
    elif function == '11':
        def clock():
            print('''
                    *****************************************************
                                Clock
                    *****************************************************
                    1.Alarm clock
                    2.Clock settings
                    3.Date settings
                    4.Stopwatch
                    5.Countdown timer
                    6.Auto update of date and time
                    7.Home
                    *****************************************************
                       *Select a function using the number beside it*
                    *****************************************************
                    ''')
            function = input('Enter number: ')
            if function == '1':
                under_construction('Alarm clock')
                return clock()
            elif function == '2':
                under_construction('Clock settings')
                return clock()
            elif function == '3':
                under_construction('Date settings')
                return clock()
            elif function == '4':
                under_construction('Stopwatch')
                return clock()
            elif function == '5':
                under_construction('Countdown timer')
                return clock()
            elif function == '6':
                under_construction('Auto update of date and time')
                return clock()
            elif function == '7':
                return home()
            else:
                return clock()
        clock()
    elif function == '12':
        under_construction('Profiles')
        return home()
    elif function == '13':
        under_construction('SIM services')
        return home()
    elif function == '14':
        exit()
    else:
        return home()


def phonebook():
    print('''
    *****************************************************
                Phone book
    *****************************************************
    1.Search
    2.Service Nos.
    3.Add name
    4.Erase
    5.Edit
    6.Assign Tone
    7.Send b'card
    8.Options
    9.Speed dials
    10.Voice tags
    11.Home
    *****************************************************
        *Select a function using the number beside it*
    *****************************************************
    ''')
    function = input('Enter number: ')
    if function == '1':
        under_construction('Search')
        return phonebook()
    elif function == '2':
        under_construction('Service Nos.')
        return phonebook()
    elif function == '3':
        under_construction('Add name')
        return phonebook()
    elif function == '4':
        under_construction('Erase')
        return phonebook()
    elif function == '5':
        under_construction('Edit')
        return phonebook()
    elif function == '6':
        under_construction('Assign tone')
        return phonebook()
    elif function == '7':
        under_construction("Send b'card")
        return phonebook()
    elif function == '8':
        options()
    elif function == '9':
        under_construction('Speed dials')
        return phonebook()
    elif function == '10':
        under_construction('Voice tags')
        return phonebook()
    elif function == '11':
        return home()
    else:
        return phonebook()


def options():
    print('''
    *****************************************************
                Options
    *****************************************************
    1.Type of view
    2.Memory status
    3.Back
    4.Home
    *****************************************************
        *Select a function using the number beside it*
    *****************************************************
    ''')
    function = input('Enter number: ')
    if function == '1':
        under_construction('Type of view')
        return options()
    elif function == '2':
        under_construction('Memory status')
        return options()
    elif function == '3':
        return phonebook()
    elif function == '4':
        return home()
    else:
        print('Invalid input')
        return options()

def messages():
    print('''
        *****************************************************
                    Messages
        *****************************************************
        1.Write messages
        2.Inbox
        3.Outbox
        4.Picture Messages
        5.Templates
        6.Smileys
        7.Message settings
        8.Info service
        9.Voice mailbox number
        10.Service command editor
        11.Home
        *****************************************************
            *Select a function using the number beside it*
        *****************************************************
        ''')
    function = input('Enter number: ')
    if function == '1':
        under_construction('Write messages')
        return messages()
    elif function == '2':
        under_construction('Inbox')
        return messages()
    elif function == '3':
        under_construction('Outbox')
        return messages()
    elif function == '4':
        under_construction('Picture messages')
        return messages()
    elif function == '5':
        under_construction('Templates')
        return messages()
    elif function == '6':
        under_construction('Smileys')
        return messages()
    elif function == '7':
        message_settings()
    elif function == '8':
        under_construction('Info service')
        return messages()
    elif function == '9':
        under_construction('Voice mailbox number')
        return messages()
    elif function == '10':
        under_construction('Service command editor')
        return messages()
    elif function == '11':
        return home()
    else:
        return messages()

def message_settings():
    print('''
    *****************************************************
                Message settings
    *****************************************************
    1.Set
    2.Common
    3.Back
    4.Home
    *****************************************************
        *Select a function using the number beside it*
    *****************************************************
    ''')
    function = input('Enter number: ')
    if function == '1':
        def set():
            print('''
            *****************************************************
                        Set
            *****************************************************
            1.Message center number
            2.Message sent as
            3.Message validity
            4.Back
            5.Home
            *****************************************************
                *Select a function using the number beside it*
            *****************************************************
            ''')
            function = input('Enter number: ')
            if function == '1':
                under_construction('Message center number')
                return set()
            elif function == '2':
                under_construction('Message sent as')
                return set()
            elif function == '3':
                under_construction('Message validity')
                return set()
            elif function == '4':
                return message_settings()
            elif function == '5':
                return home()
            else:
                return set()
        set()
    elif function == '2':
        def common():
            print('''
            *****************************************************
                        Common
            *****************************************************
            1.Delivery reports
            2.Reply via same center
            3.Character support
            4.Back
            5.Home
            *****************************************************
                *Select a function using the number beside it*
            *****************************************************
            ''')
            function = input('Enter number: ')
            if function == '1':
                under_construction('Delivery reports')
                return common()
            elif function == '2':
                under_construction('Reply via same center')
                return common()
            elif function == '3':
                under_construction('Character support')
                return common()
            elif function == '4':
                return message_settings()
            elif function == '5':
                return home()
            else:
                return common()
        common()
    elif function == '3':
        return messages()
    elif function == '4':
        return home()
    else:
        return message_settings()


def nokia():
    power = input('Enter 1 to on the phone: ')
    if power == '1':
        home()
    else:
        exit()


nokia()
