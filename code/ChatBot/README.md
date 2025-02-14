# Chatbot

Mengyao Zhang

eid: mz22984

<!-- vscode-markdown-toc -->
* 1. [How the Chatbot Works](#HowtheChatbotWorks)
* 2. [What Makes Each Personality Unique](#WhatMakesEachPersonalityUnique)
* 3. [Extra Features](#ExtraFeatures)
	* 3.1. [A Third Personality Type:](#AThirdPersonalityType:)
	* 3.2. [A Way to Switch Between Personalities:](#AWaytoSwitchBetweenPersonalities:)
	* 3.3. [Special Commands ("/help"):](#SpecialCommandshelp:)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

##  1. <a name='HowtheChatbotWorks'></a>How the Chatbot Works
This chatbot operates by engaging in a conversation with the user, maintaining a record of the last few messages exchanged. When a user sends a message, it stores their input, creates a prompt, and sends it to the LLM (Large Language Model) API to generate a response. The conversation history helps the chatbot provide more context-aware replies, making interactions feel more natural. The chatbot also retains a memory of the previous three exchanges to keep the conversation flowing smoothly.

##  2. <a name='WhatMakesEachPersonalityUnique'></a>What Makes Each Personality Unique
The chatbot has three distinct personalities, each designed for a different interaction style:

1. Friendly Bot: This personality is casual and approachable, always ready with a friendly tone. It makes conversations feel comfortable and supportive, perfect for informal chats.

2. Teacher Bot: The Teacher Bot is more formal and informative, ideal for explaining topics in detail. It provides educational content with clarity, particularly tailored to the subject it's teaching.

3. Assistant Bot: A helpful, service-oriented personality designed to assist the user with a variety of tasks. It's polite, efficient, and always ready to lend a hand with anything the user needs.

##  3. <a name='ExtraFeatures'></a>Extra Features
###  3.1. <a name='AThirdPersonalityType:'></a>A Third Personality Type: 
In addition to the Friendly and Teacher Bots, we've added an Assistant Bot personality. This bot focuses on helping users with tasks and answering queries in a more formal, service-driven way.

###  3.2. <a name='AWaytoSwitchBetweenPersonalities:'></a>A Way to Switch Between Personalities: 
Users can easily switch between the different personalities by typing the special command /change. This will reset the conversation and prompt the user to select a new bot personality, offering flexibility in interaction style based on user preference.

###  3.3. <a name='SpecialCommandshelp:'></a>Special Commands ("/help"): 
Special commands like /help provide additional user guidance, displaying available commands and how to interact with the bot. The /quit command allows the user to exit the chat, and /change allows switching the chatbot personality mid-conversation, giving the user greater control over their interaction experience.