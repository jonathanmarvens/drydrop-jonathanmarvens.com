date: 2012-09-17 11:07
title: A New Password System
tags: security, intelligence
slug: a-new-password-system
category: technology

Ever since I've been using [computers][], it has all been a wonder for me. I use computers, with the help of the amazing "[internet][]" [;)], to check my emails, watch videos, stream music, read books, etc. I've always been [happy][] with the way things normally just work.

Dedicated programmers/developers all over the world have taken their time to develop the sophisticated systems we use today. Today, when you buy a copy of Microsoft Office, for example, dedicated Microsoft Office developers from a Microsoft team have taken their time to make sure that when anyone pops open the software, it just works. The same goes for Apple or any other company. Now, these things are good and it is great that we have systems that can do all our work for us, but with that comes a big issue.

The more sophiscated our systems get and the more work they do for us, the more we rely on them for certain things. We are now relying so much on these systems that most of us nowadays could not remember a phone number if we were to be paid to do so. A recent [study by scientists shows that as much as `295 exabytes`][1] of data has been stored on systems all around the world as of 2007.

Allow me to clarify how much data that is.

	1 terabyte		~= 1,000 gigabytes
	1 gigabyte		~= 1,000 megabytes

	295 exabytes	~= 295,000,000 terabytes ~= 295,000,000,000 gigabytes

The average laptop, nowadays, is shipped with a storage capacity of `250 GB` - `500 GB`. Let's make believe that every computer running in the world had `320 GB` of storage capacity. Based on this study, it would mean that `~ 921,875,000` (`295000000000 / 320 ~= 921875000`) people in this world are saving `~ 320 GB` of data, each, on these systems.

Long story, short, **WE'RE BEGINNING TO DEPEND TOO MUCH** and **STORING TOO MUCH DATA** on these systems! And don't forget that the real danger is that these systems are [getting smarter][] everyday now with [artificial intelligience][].

The question is, what will happen to all this data when our own computers and robots take over the world? How will we protect ourselves if even our precious and important data, like our passwords, for example, we have to retrieve from them?

![Terminator](/static/public/a-new-password-system-terminator.jpg)

Let's get to the subject of this article: passwords. I believe that probably `~ 80%-90%` of time spent on a computer by the average person, nowadays, is spent browsing the web. Probably `~ 75%-85%` of websites require a login of some kind. This login usually includes a username and a password.

Most of us, at some point in our lives, have been given this one, great, piece of advice about passwords: *"Don't use the same password on different websites."*.

This might be very easy to say, but it is very hard to accomplish. We are humans (for the most part...[:)]). Our brains has limits on how much can be stored and remembered.

For example, if an average person were to use about 25 websites on average, how do you expect that person to memorize 25 different passwords. Quite simply, I don't think that's possible.

I would like to take myself as an example. As a programmer with a very good amount of knowledge in security, I have always known not to use the same password on different websites and services. However, simply knowing that never did me any good. I tried it, but I had to reset my passwords so much on the websites and services that I just gave up. I just couldn't do it.

I now have a solution! For the past couple months or so, I've been hanging out a lot with this cool guy, [Michael Bourque][]. Due to some things we've been doing, I've been able to see a couple of his passwords. Well, he would have passwords that, to me, looked like complete giberish, yet he never have a problem remembering them. After questioning Michael about this a couple of times, one day, he gave me his **secret**: he created his own *password system*.

The password system works like this:

1. Build a personal system of character replacements.
	- For example:
	<pre>
	[
		'q' => '@',
		'w' => '&',
		'e' => '9',
		'r' => '%',
		't' => '7',
		'y' => '$',
		...
	]
	</pre>
2. Take some time to use and memorize your character replacements.
3. Construct a password pattern.
	- For example, you might decide to use one word (or group of words) in a pattern like this:
		- `#$Bacon&Cheese_${{site}}!`:
			- Here,`{{site}}` will be replaced by an actual website name, like `google.com`.
		- `~&J$-{{computer_name}}@`:
			- Here,`{{computer_name}}` will be replaced by an actual computer name, like `macbook-work`.
4. Take some time to use and memorize your password pattern.
5. Construct different password patterns for other situations.
	- For example, you have an account on Facebook and that annoying girlfriend of yours won't stop demanding your password. For a situation like that, you might decide to create a new pattern with her name in it and make her happy (it's just an example...don't it personal).
		- `*@!IluvMary--facebook.com##`:
			- Here, `Mary` is your girlfriend's name and `facebook.com` is the website this password is for.
6. Construct a pattern for resetted passwords.
	- I could give an example, but I'm going to leave that to you to figure out. [:)]

I've now been able to construct my own, similar, system and have been using that since without **any** issues.

So I encourage you, stop registering passwords as `iluvmymomma1` and consider using a system like this for you privacy, safety, and security.

Once you have accomplish these things, I guarantee you that you will be feeling **[awesome][]**! Just make sure you never tell or show anyone your charater replacements or password pattern and you'll be all set.

Also, keep in mind that if you do use this, in 2020, when Sammy the Robot tries to brute force your Facebook account to stalk your friends and make your life miserable, he'll process so hard his metal head will burst, causing his positive and negative leads to contact which in turn will cause a short circuit, and he'll never be able to have robotic children. **Total**...**WIN**!

Any comments, suggestions, criticism (yes, that), or thoughts are welcome. Please feel free to comment below.

[computers]: http://en.wikipedia.org/wiki/Computer
[internet]: http://en.wikipedia.org/wiki/Internet
[happy]: http://www.youtube.com/watch?v=1YAzAu3Ut6c
[1]: http://www.bbc.co.uk/news/technology-12419672
[getting smarter]: http://www.youtube.com/watch?v=_ySljCcnq4o
[artificial intelligience]: http://en.wikipedia.org/wiki/Artificial_Intelligence
[Michael Bourque]: http://www.linkedin.com/in/mbourque
[awesome]: http://www.youtube.com/watch?v=SH6So3QOK9U