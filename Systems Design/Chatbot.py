'''
https://www.tidio.com/blog/chatbot-design/
Originally Microsoft offered help from real agents via live chat. Over time, an increasing
portion of recurring queries could be resolved by chatbot.
Now, virtual assistant is the primary
Sometimes online customer service can be tedious and repetitive
Chatbots are computer programs that simulate human conversations
Benefits
    - Increased Customer engagement (compared to emails)
    - 24/7 availability and realtime support
    - Personalized customer experiences
        - For new customers
        - Returning customers
        - shoppers who abandoned shopping carts
        - Chatbots can be configured to keep track of products customers have viewed or bought in the past
        - Bots can then make future recommendations based on that data.
        Ecommerce chatbots can identify customers, offer personalized messages and can even address
        visitors by their first name

    - Can be used for automated sales campaigns
    - Increased productivity of customer support teams
    - Reduced operational costs
    - Embedded chat box can also collect data about the customer including what they are doing on the
    website etc.,

If you want to use chatbots for business, you first need to add a live chat to your website and social media
Live chat can be added by adding a live chat widget tidio.com/blog/chat-widgets/

1. Make sure you really need a chatbot
    Do I really need a chatbot for that?
    Keep it simple, clean out the banter, send clear direct messages, not too chatty
    If too many products, then provide a search bar and product category pages
2. Choose the right platform and framework
3. Determine if you need AI or NLP (Natural language processing) or simple decision chatbot
4. setup goals and stick to them
    A good chatbot is designed to perform one task at a time
    Most popular chatbot goals are
        Generating leads
        Showing featured products
        Booking meetings and demos
        Answering FAQs
        Rescuing abandoned shopping carts
        collecting feedback
    It is better to use a dedicated chatbot for each and every goal
    For example, trigger a lead-generating chatbot when someone visits the website, when they scrolldown
    to the bottom of the page, another chatbot can collect reviews can pop up
5. Consider the tone and voice
6. UI is friendly and readable
7. Tell your customers they are talking to a chatbot
8. Keep chatbot conversation flows to simple and to the point
9. Use visuals for better effect
    The pacing and visual effects make customers more engaged and drawn into exchange of messages
10. Conduct A/B testing (pronounced AB testing) to see which messages work
11. Design a chatbot that matches the personality
    Can use chatbot avatars - it is like icing on the cake
    It is more memorable and fun to interact with
    When user sees a character - even if it is just a cartoon dog or a robot -
        it is much easier to channel their emotions
    Still, we should be careful. If we use a chatbot instead of an impersonal abstract interface,
        people will connect with it on a deeper level. It means easier to get angry at it too..
        (Microsoft office virtual assistant Clippy was most despised)

12. leave a possibility to contact a human support agent too
    It is important to know if something should be a chatbot(first step)
    It is also equally important to retreat and hand the conversation over
    When user can't get the right information after numerous efforts , it is deeply frustrating and
    happens all too often
    It is perfectly ok for chatbot to say "I am sorry, but I cannot help you.
    Would you like to contact a live agent?"
'''


'''
Design a conversational chatbot
https://medium.com/voice-tech-podcast/conversation-design-workflow-how-to-design-your-chatbot-in-10-basic-steps-721652b056d
1. Goals and KPIs (Key Performance Indicator) - Understand the main goals of your conversation interface
    main goal can be to sell something, to book a flight or a medical examination, 
    to help users navigate a website and find information quickly or to engage them in
    long conversation to generate leads
    Collect business requirements
        - needs and expectations
        - The idea of goal achievement
    Consider if these goals are good fit for the chatbot or a voice bot.
        - If expectations are not a good fit or realistic or cannot be met with conversation product,
            you should make it clear from the beginning
            
2. User research and User personas
    Find target users
    If unable to interview or submit question forms to future users, analyze contact history
     (emails, tickets that contact center receives) and see what people actually want
    With Research, start putting down some characteristics and see if they match
        Who are the chatbot target users
        what do they ask and what do they need
        how do they ask questions
    At the end of the analysis, start defining some user personas such as age, gender, language and 
    culture, profession and hobbies, geography
          
3. Topics mapping
    Will the bot be a generalist or specialist?
    Will it answer wide range of questions or limited set of topics?
    Note that conversational interfaces cannot deal with the entire human knowledge
    There can be syntactic ambiguity. Many words can indeed have different meanings, 
    so , it is better to narrow down the context
    
4. Bot personality and tone of voice
    Your bot should speak the same language your target users speak and its overall personality should
    reflect the brand you are working for?
    Decide
        Formal or informal
        Serious or fun
        verbose or concise
    Choices made here will influence all the stylistic choices that we make while writing the copy and
    design flows
    Try to give bot a human voice so users can establish a emotional connection
    Creating a bot personality will also keeps the consistency if more people are working on the project
    
5. User flows design
    It means creating architecture behind everything that a conversational bot does or says
    It defines how the  bot will introduce itself and how it will answer questions
    It also defines how to retrieve information, what conditions are taken into consideration before answering
    and how users will be guided to achieve goals
    
    Conversation designers need to design repairs sequences
        Find a way to fail gracefully when a bot doesn't understand what a user says
        
    Be honest and short - Dont blame user and dont apologize too much
    Suggest how to continue the conversation - Specify what bot can do, what questions user can ask
        and how they can ask
    Give an opportunity to connect to a human - email or live chat or phone number so users feel heard
    and they will be taken care of and their wishes will be satisfied
    
6. Prompts and copy writing
    People do not read!!
    Be clear and concise in few sentences
    Allow users to ask more.. maybe a button "I want to know more"
    Be consistent with the personality and tone of the voice you chosen
    Allowed to use abbreviation, emojis and characteristics of spoken variety 
    
7. Prototype and test with users
    Time for an early test
    For chatbot, a prototype to test its visual elements
    For voicebot, speech synthesis tool to record answers
    
    The best way to test a conversational interface is to use wizard of oz method
    The Wizard of Oz method is a moderated research method in which a user interacts 
    with an interface manned by a human who controls the system responses.
    
    the sooner the tests the better
    to find out what flows and wordings do not work, and change them before they are implemented
    
8. Setup the NLU
    Natural language understanding is the component that allows a bot to understand
    inputs expressed in natural language
    
    not all bots are NLUs eg: some where users can only select options
    NLUs needs training set of phrases to give to the machine learning algorithm
    
9. Implement the flows
    Not a conversational designer's job
    Once designed, it will be handed over to developers
    Sometimes designers will implement with tools that do not require coding skills
    
    To choose the right builder, consider following elements
         Channels: Do you need the bot to be on social media 
            (fb, messenger, whatsapp, skype or website, on alexa or other channels?)
            Some builders give more features than others
        NLU: NLU or planned paths?
        Personalization: What degree of personalization do your conversations need?
            will users be called by name?
            will they be greeted differently depending on the time of the day? season, year
            some bot builders allow use of this information
        Operations: What kind of operations will the bot perform?
            Some bots are great for FAQ but dont allow sending emails, subscribing to newsletters,
            giving details about orders etc..
            
10. Go live, analyze and iterate
    Analyze real conversations
    understand how chatbot is performing
    see if design choices can be improved
            
'''
'''
https://acquire.io/blog/chatbot-design

4. Study the intricacies of user statements
    imagine you have trained your chatbot to understand the sentences 
        “I want to see the balances of my 401k” or 
        “Can I enroll in 401k?” or 
        “What are the terms and conditions of my 401k?” 
    And then, someone comes along and asks, “I want help with my 401k.”
    Unlike a human, the chatbot will probably find this statement too generic to understand. 
    It needs to have a built-in way to disambiguate user statements – 
    to find the meaning behind what is said. 
    
    There are two ways you can resolve this when designing a chatbot:
    1. Populate a menu of 401k questions any time a person asks a question with the word “401k”. 
    This is the easiest way since the message will be the same each time. 
    But, this isn’t the greatest experience, because if someone does actually say, 
    “I want to enroll in a 401k,” it’ll most likely be frustrating to scroll through a menu.
    
    2. Incorporate models and logic that will look at questions and match them to your database of 
    existing answers. With this method, if the user asks something and there's only one answer 
    that's relevant, the bot will always respond with that answer. 
    If they ask something where several answers may be possible, the bot can either come back 
    to the person and say “Hey, could you please elaborate with more details?” or 
    respond with “Here's everything I can answer about 401k.”
    
5. Find ways to handle fragmented messages
    “The chatbot could wait maybe two or three seconds and group whatever the user said together,”
    this might end up making the performance worse, because the chatbot may be confused if users 
    ask more than one question at the same time. Maybe the chatbot has a match for one question 
    but not for the other.
    
    So you might be more successful in trying to resolve this by informing the user about what the 
    chatbot can help them with and let them click on an option. 
      
    



'''