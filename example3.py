# -*- coding: utf-8 -*-
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E3'
strategy_name = 'Collude but retaliate'
strategy_description = '''\
Collude first round. Collude, except in a round after getting 
a severe punishment.'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' # Betray if they were severely punished last time,
    else:
        return 'c' #### Romeo and Juliet By William Shakespeare
#Verona, Italy—1590's, July
""" ROMEO ..........................Son of MONTAGUE
BENVOLIO.....................Montague cousin of ROMEO
BALTHASAR .................Montague servant to ROMEO
ABRAM ..........................Montague servant
LORD MONTAGUE.......Father of ROMEO
LADY MONTAGUE.......Mother of ROMEO
JULIET............................Daughter of CAPULET, age 13
TYBALT.........................Capulet cousin of JULIET
SAMPSON......................Capulet servant
GREGORY......................Capulet servant
LORD CAPULET ...........Father of JULIET, in his 50's
LADY CAPULET ...........Mother of JULIET, about 27
NURSE ...........................Capulet servant to JULIET
PETER ............................Capulet servant to NURSE
MERCUTIO ....................Friend of ROMEO, related to PRINCE
COUNTY PARIS ............Count to wed JULIET, related to PRINCE
PRINCE ESCALUS.........Prince of Verona
FRIAR LAWRENCE.......Franciscan who marries ROMEO & JULIET
FRIAR JOHN ..................Carries message for FRIAR LAWRENCE
APOTHECARY ..............Sells poison to ROMEO
CITIZENS, SERVANTS, MUSICIANS, GUARDS, etc.
Shakespeare’s complete original script based on the Second Quarto of 1599, with corrections
and alternate text from other editions indicated as:
1First Quarto of 1597; 2
Second Quarto of
1599; 3
Third Quarto of 1609, 4Fourth Quarto of 1622, 5First Folio of 1623, and +
 for later
editions. First performed around 1595. Line-numbering matches the Folger Library edition
of 1992. Spelling and punctuation are modernized (American) with some indications of
pronunciation. Stage directions are clarified. Side notes are given for vocabulary, figurative
language, and allusions. This script be downloaded from www.hundsness.com and used
freely for education and performance. David Hundsness, editor, 2004. 
PROLOGUE
CHORUS 1.0.1
Two households, both alike in dignity, families, rank
In fair Verona, where we lay our scene,
From ancient grudge break to new mutiny, rivalry, outbreaks, fighting
Where civil blood makes civil hands unclean. civilian
From forth the fatal loins of these two foes fateful, children 1.0.5
A pair of star-cross'd lovers take their life, doomed
Whose misadventured piteous overthrows unfortunate, pitiful, downfall
Doth2
 with their death bury their parents' strife. do+
, end, fighting
The fearful passage of their death-mark'd love, doomed
And the continuance of their parents' rage, 1.0.10
Which, but their children's end, naught could remove, except for, nothing
Is now the two hours' traffic of our stage. performance
The which if you with patient ears attend, listen
What here shall miss, our toil shall strive to mend. play
ACT 1, SCENE 1
[Verona, a street, morning. SAMPSON & GREGORY, armed]
SAMPSON 1.1.1
Gregory, on my word, we'll not carry coals. take insults
GREGORY 1.1.2
No, for then we should be colliers. coal miners
SAMPSON 1.1.3
I mean, if5
 we be in choler, we'll draw. and2
, angered, draw our weapons
GREGORY 1.1.4
Ay, while you live, draw your neck out of [the]1
 collar. take, noose
SAMPSON 1.1.6
I strike quickly, being moved. attack, angered
GREGORY 1.1.7
But thou art not quickly moved to strike.
SAMPSON 1.1.8
A dog of the house of Montague moves me.
GREGORY 1.1.9
To move is to stir, and to be valiant is to stand. brave
Therefore if thou art moved, thou runn'st away!
SAMPSON 1.1.12
A dog of that house shall move me to stand. I will
take the wall of any man or maid of Montague's. make them step aside
GREGORY 1.1.14
That shows thee a weak slave2
, for the weakest weakling1
: coward
goes to the wall. backs up against the wall
SAMPSON 1.1.16
'Tis true, and therefore women, being the weaker vessels, gender
are ever thrust to the wall. Therefore I will push Montague's always
men from the wall, and thrust his maids to the wall. women
GREGORY 1.1.20
The quarrel is between our masters and us their men. menservants
SAMPSON 1.1.22
'Tis all one. I will show myself a tyrant. When I all the same, prove
have fought with the men, I will be civil with the humane
maids, and5
 cut off their heads! I will2
GREGORY 1.1.25
The heads of the maids? 
SAMPSON 1.1.26
Ay, the heads of the maids, or their maidenheads! virginity
Take it in what sense thou wilt. whatever meaning
GREGORY 1.1.28
They must take it in1
 sense that feel it! feel what I do to them (bawdy)
SAMPSON 1.1.29
Me they shall feel while I am able to stand, and
'tis known I am a pretty2
 piece of flesh. tall1
(bawdy)
GREGORY 1.1.31
'Tis well thou art not fish; if thou hadst, if you were
thou hadst been poor-john. a poor catch
[ABRAM & another Montague Servant enter, armed]
Draw thy tool! Here comes [two]1
 of the house of Montagues2
! sword, the Montagues5
SAMPSON 1.1.34
My naked weapon is out. Quarrel, I will back thee. unsheathed, fight
GREGORY 1.1.36
How, turn thy back and run? how do you mean
SAMPSON 1.1.37
Fear me not. trust me
GREGORY 1.1.38
No, marry. I fear thee! indeed
SAMPSON 1.1.39
Let us take the law on1
 our side1
; let them begin. of2
, sides2
GREGORY 1.1.41
I will frown as I pass by, and let them take it as they list. please
SAMPSON 1.1.43
Nay, as they dare. I will bite my thumb at them, give the finger
which is a disgrace to them if they bear it. take it without a fight
[bites his thumb]
ABRAM 1.1.45
Do you bite your thumb at us, sir?
SAMPSON 1.1.46
I do bite my thumb, sir.
ABRAM 1.1.47
Do you bite your thumb at us, sir?
SAMPSON [aside to Gregory] 1.1.48
Is the law on1
 our side if I say "ay"? of2
, yes
GREGORY [aside to Sampson] 1.1.50
No!
SAMPSON 1.1.51
No, sir, I do not bite my thumb at you, sir, but I bite my
thumb, sir.
GREGORY 1.1.53
Do you quarrel, sir? challenge us
ABRAM 1.1.54
Quarrel sir? No, sir!
SAMPSON 1.1.55
But if you do, sir, I am for you! I serve will fight you
as good a man as you. master
ABRAM 1.1.57
No better?
SAMPSON 1.1.58
Well, sir—
GREGORY [sees Tybalt coming; to Sampson] 1.1.59
Say "better"! Here comes one of my master's kinsmen. relatives
SAMPSON 1.1.61
Yes, better, [sir]2
.
[not in 5]
ABRAM 1.1.62
You lie! 
SAMPSON 1.1.63
Draw, if you be men!
Gregory, remember thy washing blow. slashing stroke
[They fight]
BENVOLIO [enters, sword drawn] 1.1.65
Part, fools! separate
Put up your swords! You know not what you do! put away
TYBALT [enters, to Benvolio] 1.1.67
What, art thou drawn among these heartless hinds? deer/servants
Turn thee, Benvolio. Look upon thy death! face your death
[draws his sword]
BENVOLIO 1.1.69
I do but keep the peace. Put up thy sword, just, put away
Or manage it to part these men with me. use
TYBALT 1.1.71
What, drawn, and talk of peace? I hate the word, your sword drawn
As I hate hell, all Montagues, and thee!
Have at thee, coward!
[They fight]
CITIZENS [enter, armed] 1.1.74
Clubs, bills, and partisans! Strike! Beat them down! weapons
Down with the Capulets! Down with the Montagues!
[LORD & LADY CAPULET and LORD & LADY MONTAGUE enter]
CAPULET 1.1.76
What noise is this? Give me my long sword, ho! outdated weapon
LADY CAPULET [mocking his old age] 1.1.77
A crutch, a crutch! Why call you for a sword?
CAPULET 1.1.79
My sword, I say! Old Montague is come
And flourishes his blade in spite of me! waves, to spite
MONTAGUE 1.1.81
Thou villain Capulet! [she stops him] Hold me not, let me go!
LADY MONTAGUE 1.1.82
Thou shalt not stir one2
 foot to seek a foe! a
5
PRINCE [enters with Attendants] 1.1.83
Rebellious subjects, enemies to peace,
Profaners of this neighbor-stainèd steel offenders, bloody
—Will they not hear?—What, ho! You men, you beasts,
That quench the fire of your pernicious rage deadly
With purple fountains issuing from your veins! pouring
On pain of torture, from those bloody hands
Throw your mistempered weapons to the ground, hostile
And hear the sentence of your movèd Prince! angered 1.1.90
Three civil brawls, bred of an airy word public, started by few words
By thee, old Capulet, and Montague,
Have thrice disturbed the quiet of our streets, three times
And made Verona's ancient citizens oldest
Cast by their grave-beseeming ornaments, put aside their dignity 1.1.95
To wield old partisans, in hands as old, weapons
Cankered with peace, to part your cankered hate. infected, infectious
If ever you disturb our streets again,
Your lives shall pay the forfeit of the peace! you'll be executed for
For this time, all the rest depart away. for now, the rest of you 1.1.100
You Capulet, shall go along with me,
And Montague, come you this afternoon,
To know our further+
 pleasure in this case, my, farther2
/father's5
, decisions
To old Freetown, our common judgment-place. public court
Once more, on pain of death, all men depart!
[All exit but Lord & Lady Montague and Benvolio] 
MONTAGUE2
 [to Benvolio] LADY MONTAGUE1
 1.1.106
Who set this ancient quarrel new abroach? in action again
Speak, nephew, were you by when it began? nearby
BENVOLIO 1.1.108
Here were the servants of your adversary,
And yours, close fighting ere I did approach. before
I drew to part them. In the instant came
The fiery Tybalt, with his sword prepared, fiery-tempered, drawn
Which, as he breathed defiance to my ears,
He swung about his head and cut the winds
Who, nothing hurt withal, hissed him in scorn. not hurting anyone
While we were interchanging thrusts and blows,
Came more and more and fought on part and part, people, on each side
Till the Prince came, who parted either part. both sides
LADY MONTAGUE 1.1.118
O, where is Romeo? Saw you him today?
Right glad I am he was not at this fray. fight
BENVOLIO 1.1.120
Madam, an hour before the worshipped sun
Peered forth the golden window of the east, from
A troubled mind drove+
 me to walk abroad, drave3
, around
Where, underneath the grove of sycamore
That westward rooteth from the city's side, grows west of the city
So early walking did I see your son. 1.1.125
Towards him I made, but he was 'ware of me walked, aware
And stole into the covert of the wood. hid in the woods
I, measuring his affections by my2
 own, guessing, mood, mine1
Which then most sought where most might not be found, wanted to be
Being one too many by my weary self, not wanting company
Pursued my humor2
 not pursuing his, followed, honor1,5: mood, questioning
And gladly shunned who gladly fled from me. avoided him
MONTAGUE 1.1.134
Many a morning hath he there been seen,
With tears augmenting the fresh morning dew, adding to
Adding to clouds more clouds with his deep sighs.
But all so soon as the all-cheering sun as soon as
Should in the furthest east begin to draw
The shady curtains from Aurora's bed, god of dawn
Away from the light steals home my heavy son, comes home, sad 1.1.140
And private in his chamber pens himself, bedroom, locks
Shuts up his windows, locks fair daylight out,
And makes himself an artificial night.
Black and portentous must this humor prove, foreboding, mood
Unless good counsel may the cause remove. advice, remove the cause
BENVOLIO 1.1.146
My noble uncle, do you know the cause?
MONTAGUE 1.1.147
I neither know it nor can learn of him. learn it from him
BENVOLIO 1.1.148
Have you importuned him by any means? questioned
MONTAGUE 1.1.149
Both by myself and many other friends.
But he, his3
 own affections' counselor, mood's
Is to himself—I will not say how true— keeps to himself, true to himself
But to himself so secret and so close, only, closed
So far from sounding and discovery, reasoning, understanding
As is the bud bit with an envious worm vicious
Ere he can spread his sweet leaves to the air, before it, its
Or dedicate his beauty to the sun+
. same2
Could we but learn from whence his sorrows grow, if we could only, where
We would as willingly give cure as know.
[ROMEO enters]
BENVOLIO 1.1.159
See where he comes. So please you, step aside. look, he's coming
I'll know his grievance or be much denied. the cause of his distress
MONTAGUE 1.1.161
I would thou wert so happy by thy stay wish, successful
To hear true shrift.—Come, madam, let's away. confessions
[They exit]
BENVOLIO 1.1.163
Good morrow, cousin. good morning
ROMEO Is the day so young? 1.1.164
BENVOLIO 1.1.165
But new struck nine. just now
ROMEO Ay me, sad hours seem long. 1.1.166
Was that my father that went hence so fast? away
BENVOLIO 1.1.168
It was. What sadness lengthens Romeo's hours?
ROMEO 1.1.169
Not having that, which having, makes them short.
BENVOLIO 1.1.170
In love?
ROMEO 1.1.171
Out—
BENVOLIO 1.1.172
Of love?
ROMEO 1.1.173
Out of her favor where I am in love.
BENVOLIO 1.1.174
Alas, that Love, so gentle in his view, too bad Cupid who looks gentle
Should be so tyrannous and rough in proof! is actually rough
ROMEO 1.1.176
Alas, that Love, whose view is muffled still, blindfolded, always
Should, without eyes, see pathways to his will! purposes
Where shall we dine?
[sees signs of the fight] O me! What fray was here?
Yet tell me not, for I have heard it all.
Here's much to do with hate, but more with love. it's all about 1.1.180
Why, then, O brawling love, O loving hate,
O anything of nothing first create1
! created2
: created of nothing
O heavy lightness, serious vanity, foolishness
Misshapen chaos of well-seeming4
 forms, attractive
Feather of lead, bright smoke, cold fire, sick health, 1.1.185
Still-waking sleep that is not what it is! always
This love feel I, that feel no love in this. I love one who does not love me
Dost thou not laugh?
BENVOLIO No coz, I rather weep. cousin 1.1.189
ROMEO 1.1.190
Good heart, at what? friend
BENVOLIO At thy good heart's oppression. 1.1.191
ROMEO 1.1.192
Why, such is love's transgression. love's ways
Griefs of mine own lie heavy in my breast, heart
Which thou wilt propagate to have it pressed will increase, added
With more of thine. This love that thou hast shown 1.1.195
Doth add more grief to too much of mine own. 
Love is a smoke made2
 with the fume of sighs; raised1
Being purged, a fire sparkling in lovers' eyes; love being exchanged
Being vexed, a sea nourished2
 with loving2
 tears; love being denied, raging1
, lovers'1
What is it else? A madness most discreet, 1.1.200
A choking gall and a preserving sweet. bitter potion, healing sweetness
Farewell, my coz.
BENVOLIO Soft, I will go along. wait 1.1.203
And if you leave me so, you do me wrong!
ROMEO 1.1.205
Tut, I have lost myself; I am not here. nonsense
This is not Romeo; he's some other where.
BENVOLIO 1.1.207
Tell me in sadness, who is that you love? seriously
ROMEO 1.1.208
What, shall I groan and tell thee?
BENVOLIO Groan? Why no, 1.1.209
But sadly tell me who.
ROMEO 1.1.210
[Bid]
1
 a sick man in "sadness" make1
 his will? ask, makes2
A word ill-urged to one that is so ill! poorly chosen word
In sadness, cousin, I do love a woman.
BENVOLIO 1.1.213
I aimed so near when I supposed you loved.
ROMEO 1.1.214
A right good markman! And she's fair I love. marksman, beautiful
BENVOLIO 1.1.215
A right fair mark, fair coz, is soonest hit. target in plain sight
ROMEO 1.1.216
Well in that hit you miss! She'll not be hit
With Cupid's arrow. She hath Dian's wit, wisdom of Diana: god of virginity
And in strong proof of chastity well armed, armor, virginity
From Love's weak childish bow she lives uncharmed2
. Cupid's, unaffected/unharmed1
She will not stay the siege of loving terms, won't be won by sweet talk
Nor bide th'encounter of assailing eyes, loving looks 1.1.221
Nor ope her lap to saint-seducing gold. open (bawdy), riches
O, she is rich in beauty, only poor
That, when she dies, with beauty dies her store. because it dies with her
BENVOLIO 1.1.225
Then she hath sworn that she will still live chaste? always stay a virgin
ROMEO 1.1.226
She hath, and in that sparing makes4
 huge waste, withholding
For beauty, starved with her severity, sever choice
Cuts beauty off from all posterity. future generations
She is too fair, too wise, wisely too fair beautiful, just
To merit bliss by making me despair. win a place in heaven
She hath forsworn to love, and in that vow sworn not to love
Do I live dead, that live to tell it now.
BENVOLIO 1.1.233
Be ruled by me; forget to think of her. listen to me
ROMEO 1.1.234
O, teach me how I should forget to think!
BENVOLIO 1.1.235
By giving liberty unto thine eyes.
Examine other beauties!
ROMEO 'Tis the way 1.1.237
To call hers, exquisite, in question more. make me dwell on her beauty
These happy masks that kiss fair ladies' brows, lucky veils, faces
Being black, puts us in mind they hide the fair. makes us think
He that is strucken blind cannot forget 
The precious treasure of his eyesight lost. 1.1.242
Show me a mistress that is passing fair; very beautiful
What doth her beauty serve but as a note reminder
Where I may read who passed that passing fair? Rosaline who surpassed
Farewell. Thou canst not teach me to forget.
BENVOLIO 1.1.247
I'll pay that doctrine, or else die in debt. teach you that lesson, failure
[They exit]
ACT 1, SCENE 2
[A street. CAPULET, PARIS, SERVANT]
CAPULET 1.2.1
But Montague is bound as well as I required by law
In penalty alike, and 'tis not hard, I think,
For men so old as we to keep the peace.
PARIS 1.2.4
Of honorable reckoning are you both, reputation
And pity 'tis you lived at odds so long.
But now, my lord, what say you to my suit? courtship of your daughter
CAPULET 1.2.7
But saying o'er what I have said before: just saying over again
My child is yet a stranger in the world,
She hath not seen the change of fourteen years,
Let two more summers wither in their pride, pass by
Ere we may think her ripe to be a bride. before, ready
PARIS 1.2.12
Younger than she are happy mothers made.
CAPULET 1.2.13
And too soon marred are those so early made. harmed
[The]+
 earth hath swallowed all my hopes but she; grave, other children
She is+
 the hopeful lady of my earth. she's2
, of my earthly body (my offspring)
But woo her, gentle Paris, get her heart.
My will to her consent is but a part. my wishes are less important than hers
And, she agreed, within her scope of choice if she agrees
Lies my consent and fair according voice. agreeing
This night I hold an old accustomed feast, customary 1.2.20
Whereto I have invited many a guest
Such as I love; and you among the store, whom, group
One more, most welcome, makes my number more.
At my poor house look to behold this night humble, see
Earth-treading stars that make dark heaven light. beautiful women 1.2.25
Such comfort as do lusty young men feel
When well-appareled April on the heel Spring dressed in flowers
Of limping winter treads, even such delight
Among fresh female1
 buds shall you this night fennel2
: an herb inspiring passion
Inherit at my house. Hear all, all see, see, see all the women 1.2.30
And like her most whose merit most shall be; then like the best one
Which, on more view of many, mine, being one,
May stand in number, though in reck'ning none. be just one of the crowd
Come, go with me.
[to Servant, giving a paper] Go, sirrah, trudge about walk 1.2.35
Through fair Verona, find those persons out
Whose names are written there, and to them say,
My house and welcome at1
 their pleasure stay. on2
, I welcome their company
[Capulet & Paris exit]
SERVANT 1.2.39
Find them out whose names are written here! It is
written that the shoemaker should meddle with his work
yard and the tailor with his last, the fisher with yardstick, shoemaker tools
his pencil and the painter with his nets. But I am paintbrush
sent to find those persons whose names are here
writ, and can never find what names the writing written
person hath here writ. I must to the learned. go to one who can read
[BENVOLIO & ROMEO enter]
 In good time! good timing
BENVOLIO [to Romeo] 1.2.47
Tut, man, one fire burns out another's burning. nonsense
One pain is lessened by another's anguish. another pain's
Turn giddy, and be helped+
 by backward turning. dizzy, holp2
One desperate grief cures with another's languish. another grief's
Take thou some new infection to thy eye,
And the rank poison of the old will die. toxic
ROMEO 1.2.53
Your plantain leaf is excellent for that. a banana leaf (used to heal cuts)
BENVOLIO 1.2.54
For what, I pray thee? I ask you
ROMEO For your broken shin! a cut 1.2.55
BENVOLIO 1.2.56
Why, Romeo, art thou mad? going mad
ROMEO 1.2.57
Not mad, but bound more than a madman is, confined
Shut up in prison, kept without my food,
Whipped and tormented, and—
[to Servant] Good e'en, good fellow. good afternoon
SERVANT 1.2.61
God gi' good e'en. I pray, sir, can you read? God give you good afternoon
ROMEO 1.2.63
Ay, mine own fortune in my misery. I can read my fortune
SERVANT 1.2.64
Perhaps you have learned it without book. to read that by memorization
But, I pray, can you read anything you see?
ROMEO 1.2.66
Ay, if I know the letters and the language.
SERVANT 1.2.67
Ye say honestly. Rest you merry. that's honest, goodbye
ROMEO 1.2.68
Stay, fellow. I can read. [reads the list]
 "Signor Martino and his wife and daughters
 County Anselm and his beauteous sisters Count
 The lady widow of Vitruvio
 Signor Placentio and his lovely nieces
 Mercutio and his brother Valentine
 Mine uncle Capulet, his wife and daughters
 My fair niece Rosaline [and]1
 Livia
 Signor Valentino and his cousin Tybalt
 Lucio and the lively Helena"
A fair assembly. Whither should they come? pleasant group, where
SERVANT 1.2.79
Up.
ROMEO 1.2.80
Whither? To supper? where
SERVANT 1.2.81
To our house. 
ROMEO 1.2.82
Whose house?
SERVANT 1.2.83
My master's.
ROMEO 1.2.84
Indeed, I should have asked you that before.
SERVANT 1.2.85
Now I'll tell you without asking. My master is the great rich
Capulet, and if you be not of the house of Montagues, I pray,
come and crush a cup of wine. Rest you merry. [exits] drink
BENVOLIO 1.2.89
At this same ancient feast of Capulet's traditional
Sups the fair Rosaline, whom thou so loves, dines 1.2.90
With all the admired beauties of Verona.
Go thither, and with unattainted eye there, unbiased
Compare her face with some that I shall show,
And I will make thee think thy swan a crow.
ROMEO 1.2.95
When the devout religion of mine eye
Maintains such falsehood, then turn tears to fires; accepts such a lie
And these who, often drowned, could never die, my eyes will be
Transparent heretics, be burnt for liars! burnt like heretics
One fairer than my love! The all-seeing sun
Ne'er saw her match since first the world begun. anyone as beautiful
BENVOLIO 1.2.101
Tut, you saw her fair, none else being by, no one else nearby
Herself poised with herself in either eye. compared
But in that crystal scales let there be weighed
Your lady's love against some other maid
That I will show you shining at this feast,
And she shall scant show well that now seems2
 best. barely look good, shows5
ROMEO 1.2.107
I'll go along, no such sight to be shown, not to see whom you show
But to rejoice in splendor of mine own. the beauty of Rosaline
[They exit]
ACT 1, SCENE 3
[Capulet house. LADY CAPULET & NURSE]
LADY CAPULET 1.3.1
Nurse, where's my daughter? Call her forth to me.
NURSE 1.3.2
Now, by my maidenhead at twelve year old, virginity
I bade her come.—What, lamb! What, ladybird!— told
God forbid! Where's this girl?—What, Juliet!
JULIET [enters] 1.3.5
How now, who calls?
NURSE 1.3.6
Your mother.
JULIET 1.3.7
Madam, I am here. What is your will? what do you want
LADY CAPULET 1.3.8
This is the matter.—Nurse, give leave awhile, leave us
We must talk in secret.—Nurse, come back again!
I have remembered me, thou's hear our counsel. you shall, conversation
Thou know'st my daughter's of a pretty age.
NURSE 1.3.12
Faith, I can tell her age unto an hour. indeed 
LADY CAPULET 1.3.13
She's not fourteen.
NURSE 1.3.14
I'll lay fourteen of my teeth, and yet, to my teen I'll bet, suffering
be it spoken, I have but four. She's not fourteen. only four teeth
How long is it now to Lammas-tide? Lummas Day, August 1
LADY CAPULET 1.3.17
A fortnight and odd days. two weeks, a few days
NURSE 1.3.18
Even or odd, of all days in the year,
Come Lammas Eve at night shall she be fourteen.
Susan and she—God rest all Christian souls— 1.3.20
Were of an age. Well, Susan is with God;
She was too good for me. But, as I said,
On Lammas Eve at night shall she be fourteen.
That shall she. Marry, I remember it well.
'Tis since the earthquake now eleven years, 1.3.25
And she was weaned—I never shall forget it—
Of all the days of the year, upon that day.
For I had then laid wormwood to my dug, put a bitter extract on my breast
Sitting in the sun under the dove-house wall. pigeon coop
My lord and you were then at Mantua. 1.3.30
—Nay, I do bear a brain!—But, as I said, have a good memory
When it did taste the wormwood on the nipple the baby
Of my dug and felt it bitter, pretty fool, dear
To see it tetchy and fall out with the dug! irritable, refuse
"Shake," quoth the dove-house. 'Twas no need, I trow, said, believe 1.3.35
To bid me trudge. tell me to move
And since that time it is eleven years.
For then she could stand alone. Nay, by the rood, Holy Cross 1.3.40
She could have run and waddled all about,
For even the day before, she broke her brow, bumped her forehead
And then my husband—God be with his soul,
He was a merry man—took up the child.
"Yea," quoth he, "Dost thou fall upon thy face? said 1.3.45
Thou wilt fall backward when thou hast more wit, lay on your back (bawdy), learning
Wilt thou not, Jule?" And by my holy-dame, the Virgin Mary
The pretty wretch left crying and said "Ay." dear, stopped
To see now how a jest shall come about! joke, come true
I warrant, if1
 I should live a thousand years, I swear, and2
 1.3.50
I never should forget it. "Wilt thou not, Jule?" quoth he.
And, pretty fool, it stinted and said "Ay." stopped
LADY CAPULET 1.3.54
Enough of this. I pray thee, hold thy peace! I ask you, be quiet
NURSE 1.3.55
Yes, madam, yet I cannot choose but laugh, can't help but laugh
To think it should leave crying and say "Ay."
And yet, I warrant, it had upon its brow I swear
A bump as big as a young cockerel's stone, rooster's testicle
A perilous knock, and it cried bitterly. terrible
"Yea," quoth my husband, "Fall'st upon thy face? 1.3.60
Thou wilt fall backward when thou come'st to age,
Wilt thou not, Jule?" It stinted and said "Ay."
JULIET 1.3.63
And stint thou too, I pray thee, Nurse, say I! I ask you, stop
NURSE 1.3.64
Peace, I have done. God mark thee to his grace, bless you
Thou wast the prettiest babe that e'er I nursed. 
And I might live to see thee married once, if
I have my wish.
LADY CAPULET 1.3.68
Marry, that "marry" is the very theme
I came to talk of.—Tell me, daughter Juliet,
How stands your disposition to be married? how do you feel about marriage
JULIET 1.3.71
It is an honor1
 that I dream not of.
NURSE 1.3.72
An honor1
? Were not I thine2
 only nurse, thy1
, if I weren't your only wet-nurse
I would say thou hadst sucked wisdom from thy teat. the breast
LADY CAPULET 1.3.75
Well, think of marriage now. Younger than you,
Here in Verona, ladies of esteem high-breeding
Are made already mothers. By my count
I was your mother much upon these years at the same age
That you are now a maid. Thus then in brief:
The valiant Paris seeks you for his love.
NURSE 1.3.81
A man, young lady! Lady, such a man
As all the world. Why, he's a man of wax! perfect like a wax model
LADY CAPULET 1.3.83
Verona's summer hath not such a flower.
NURSE 1.3.84
Nay, he's a flower, in faith, a very flower. indeed
LADY CAPULET 1.3.85
What say you? Can you love the gentleman?
This night you shall behold him at our feast. see
Read o'er the volume of young Paris' face, read like a book
And find delight writ there with beauty's pen. written
Examine every married lineament well balanced facial feature
And see how one another lends content, each tells a story 1.3.90
And what obscured in this fair volume lies anything unclear in this book
Find written in the margent of his eyes. margins
This precious book of love, this unbound lover, uncovered/unmarried
To beautify him, only lacks a cover. he only needs a cover
The fish lives in the sea, and 'tis much pride a splendid sight 1.3.95
For fair without the fair within to hide. beauty outside is beauty within
That book in many's eyes doth share the glory a book cover is made
That in gold clasps locks in the golden story. beautiful by a beautiful tale
So shall you share all that he doth possess all his wealth and status
By having him, making yourself no less. marrying him
NURSE 1.3.101
No less? Nay, bigger. Women grow by men. get pregnant
LADY CAPULET 1.3.102
Speak briefly. Can you like of Paris' love?
JULIET 1.3.103
I'll look to like, if looking liking move, if looks will make me like him
But no more deep will I endart2
 mine eye engage1
: I won't look any deeper
Than your consent gives strength to make it1
 fly. than you want me to
SERVANT [enters] 1.3.106
Madam, the guests are come, supper served up, have come
you called, my young lady asked for, they're calling for you
the Nurse cursed in the pantry, and is being cursed
everything in extremity. I must hence is in chaos, go away
to wait. I beseech you, follow straight. wait tables, beg, right away
LADY CAPULET 1.3.111
We follow thee. [Servant exits] will follow
 Juliet, the County stays. the Count is waiting 
NURSE 1.3.112
Go, girl, seek happy nights to happy days. to make
[They exit]
ACT 1, SCENE 4
[A street, that night.
ROMEO, MERCUTIO, BENVOLIO & Others with torches and drum]
ROMEO 1.4.1
What shall this speech be spoke for our excuse? apology for intruding
Or shall we on without apology? go on into the party
BENVOLIO 1.4.3
The date is out of such prolixity. such speeches are out of date
We'll have no Cupid hoodwinked with a scarf, blindfolded
Bearing a Tartar's painted bow of lath, carrying, wood
Scaring the ladies like a crow-keeper, scarecrow
[Nor no without-book prologue, faintly spoke memorized speech
After the prompter, for our entrance.]1
But let them measure us by what they will. judge how they want
We'll measure them a measure and be gone. dance a dance
ROMEO 1.4.11
Give me a torch, I am not for this ambling. dancing
Being but heavy, I will bear the light. heavy-hearted, carry
MERCUTIO 1.4.13
Nay, gentle Romeo, we must have you dance.
ROMEO 1.4.14
Not I, believe me. You have dancing shoes
With nimble soles. I have a soul of lead
So stakes me to the ground I cannot move. that
MERCUTIO 1.4.17
You are a lover. Borrow Cupid's wings in love
And soar with them above a common bound. leap/limit
ROMEO 1.4.19
I am too sore enpiercèd with his shaft wounded, arrow
To soar with his light feathers, and so bound
I cannot bound a pitch above dull woe. leap to any height, my sorrow
Under love's heavy burden do I sink.
MERCUTIO 1.4.23
And to sink in it, should you burden love, you'd burden love by sinking in it
Too great oppression for a tender thing.
ROMEO 1.4.25
Is love a tender thing? It is too rough,
Too rude, too boisterous, and it pricks like thorn. quarrelsome
MERCUTIO 1.4.27
If love be rough with you, be rough with love!
Prick love for pricking, and you beat love down. pricking you, (bawdy)
Give me a case to put my visage in: mask, face
A visor for a visor. What care I an ugly mask for my ugly face
What curious eye doth cote deformities? eyes stare at my
Here are the beetle brows shall blush for me. here's the beetle face that'll
BENVOLIO 1.4.33
Come, knock and enter, and no sooner in, as soon as we're inside
But every man betake him to his legs. start dancing
ROMEO 1.4.35
A torch for me. Let wantons light of heart playful people
Tickle the senseless rushes with their heels, carpet
For I am proverbed with a grandsire phrase: I will follow a proverb
I'll be a candle holder and look on. (proverb)
The game was ne'er so fair, and I am done1
. party, bright (proverb)
MERCUTIO 1.4.40
Tut, dun's the mouse, a mouse is grey-brown (proverb)
 the constable's own word. so keep quiet as a mouse
If thou art Dun, we'll draw thee from the mire a horse named Dun, pull, mud
Of—save your reverence—love, wherein thou stick'st pardon me, are stuck
Up to the ears. Come, we burn daylight, ho! waste
ROMEO 1.4.45
Nay, that's not so.
MERCUTIO I mean, sir, in delay 1.4.46
We waste our lights in vain, like1
 lamps1
 by day. torches, lights2
 lights2
: lamps lit in day
Take our good meaning, for our judgment sits the obvious,
Five times in that ere once in our five+
 wits. there's much wisdom in it
ROMEO 1.4.50
And we mean well in going to this mask, masquerade party
But 'tis no wit to go. not wise
MERCUTIO Why, may one ask? 1.4.52
ROMEO 1.4.53
I dreamt a dream tonight. last night
MERCUTIO And so did I. 1.4.54
ROMEO 1.4.55
Well, what was yours?
MERCUTIO That dreamers often lie! (pun) 1.4.56
ROMEO 1.4.57
In bed asleep, while they do dream things true!
MERCUTIO 1.4.58
O, then I see Queen Mab hath been with you!
[BENVOLIO
Queen Mab? What's she?]1
MERCUTIO 1.4.59
She is the fairies' midwife, and she comes
In shape no bigger than an agate-stone gem-stone
On the forefinger of an alderman, officer
Drawn with a team of little atomies pulled by, tiny creatures
Over2
 men's noses as they lie asleep. athwart1
Her wagon-spokes made of long spinners'
2
 legs, spiders'+
 1.4.64
The cover of the wings of grasshoppers, canopy
The1
 traces of the smallest spider2
 web, her2
, harnesses, spider's5
The1
 collars of the moonshine's watery beams, her2
, harness collars, moonbeams
Her whip of cricket's bone, the lash of film, gossamer
Her wagoner a small grey-coated gnat, driver
Not half so big as a round little worm 1.4.70
Pricked from the lazy finger of a maid2
. man1
Her chariot is an empty hazelnut, 1.4.72
Made by the joiner squirrel or old grub, cabinetmaker, worm
Time out o' mind the fairies' coach-makers. for time long forgotten
And in this state she gallops night by night 1.4.75
Through lovers' brains, and then they dream of love;
O'er1
 courtiers' knees, who1
 dream on curtsies straight; on2
, that2
, right away
O'er lawyers' fingers, who straight dream on fees; right away 1.4.78
O'er ladies' lips, who straight on kisses dream, right away dream of kisses
Which oft the angry Mab with blisters plagues often, gives them blisters (herpes)
Because their breaths1
 with sweetmeats tainted are. breath2
, smell of sweet foods (bawdy)
Sometime she gallops o'er a courtier's nose,
And then dreams he of smelling out a suit; high paying job
And sometime comes she with a tithe-pig's tail pig donated to the church
Tickling a parson's nose as he+
 lies asleep, clergyman 1.4.85
Then he dreams of another benefice. getting more church money
Sometime she driveth o'er a soldier's neck,
And then dreams he of cutting foreign throats,
Of breaches, ambuscadoes, Spanish blades, crossing enemy lines, ambushes
Of healths five-fathom deep, and then anon long drinking bouts, soon
Drums in his ear, at which he starts and wakes, is startled 1.4.91
And being thus frighted swears a prayer or two
And sleeps again. This is that very Mab
That plats the manes of horses in the night, braids
And bakes the elflocks in foul sluttish hairs, mats the hair of old hags
Which once untangled, much misfortune bodes. brings misfortune (superstition)
This is the hag, when maids lie on their backs, 1.4.97
That presses them and learns them first to bear, teaches, bear children (bawdy)
Making them women of good carriage.
This is she—
ROMEO Peace, peace, Mercutio, peace! 1.4.101
Thou talk'st of nothing.
MERCUTIO True, I talk of dreams, 1.4.103
Which are the children of an idle brain,
Begot of nothing but vain fantasy, born, foolish
Which is as thin of substance as the air
And more inconstant than the wind, who woos changeable
Even now the frozen bosom of the north,
And, being angered, puffs away from thence, blows away from there
Turning his face1
 to the dew-dropping south. side2
, rainy south
BENVOLIO 1.4.111
This wind you talk of blows us from ourselves! plans
Supper is done, and we shall come too late!
ROMEO 1.4.113
I fear too early, for my mind misgives fears
Some consequence yet hanging in the stars still
Shall bitterly begin his fearful date 1.4.115
With this night's revels, and expire the term party, end the life
Of a despised life closed in my breast my hated life
By some vile forfeit of untimely death. evil, early death
But He that hath the steerage of my course
Direct my sail1
!—On, lusty gentlemen! suit2
, let's go, merry 1.4.120
BENVOLIO 1.4.121
Strike, drum! play, drummer
[All exit]
ACT 1, SCENE 5
[Capulet house. Two SERVANTS, Musicians & Guests]
1st SERVANT 1.5.1
Where's Potpan, that he helps not to take away? isn't helping to clear tables
He shift a trencher! He scrape a trencher! pick up a dish, clean a dish
2nd SERVANT 1.5.4
When good manners shall lie all in one or two men's work habits
hands, and they unwashed too, 'tis a foul thing. terrible
1st SERVANT 1.5.7
Away with the joint-stools, remove the court-cupboard, stools, sideboard
look to the plate. Good thou, save me a piece of take care of the utensils
marchpane, and as thou lovest me, let the marzipan, do me a favor, tell
porter let in Susan Grindstone and Nell. [2nd Servant exits]
Antony and Potpan!
3rd SERVANT [enters with another Servant] 1.5.12
Ay, boy, ready. 
1st SERVANT 1.5.13
You are looked for and called for, asked for and
sought for, in the great chamber. hall
3rd SERVANT 1.5.14
We cannot be here and there too. Cheerly, boys! cheer up
Be brisk awhile, and happy while you can
the longer liver take all. whoever lives longest
[They exit]
[LORD & LADY CAPULET, COUSIN CAPULET, NURSE, JULIET, TYBALT,
and more Guests enter]
CAPULET 1.5.18
Welcome, gentlemen. Ladies that have their toes
Unplagued with corns will walk a bout with you.— with no corns, dance
Ah ha, my mistresses! Which of you all ladies
Will now deny to dance? She that makes dainty, refuse, coyly refuses
She I'll swear hath corns. Am I come near you+
 now?— close to the truth, ye2
Welcome, gentlemen. I have seen the day 1.5.25
That I have worn a visor and could tell mask
A whispering tale in a fair lady's ear, beautiful
Such as would please. 'Tis gone, 'tis gone, 'tis gone. delight her
You are welcome, gentlemen!—Come, musicians, play!—
[Music plays]
A hall, a hall, give room!—And foot it, girls!— make, dance
[They dance]
More light, you knaves, and turn the tables up, idiots, fold 1.5.32
And quench the fire, the room is grown too hot.— put out
[ROMEO, MERCUTIO & BENVOLIO enter in masks]
Ah, sirrah, this unlooked-for sport comes well! servant, unexpected maskers,
[to Cousin] Nay, sit, nay, sit, good cousin Capulet, come at a good time
For you and I are past our dancing days.
How long is't now since last yourself and I
Were in a mask?
COUSIN By'r Lady, thirty years. 1.5.39
CAPULET 1.5.40
What, man, 'tis not so much, 'tis not so much.
'Tis since the nuptial of Lucentio, wedding
Come Pentecost as quickly as it will, Pentecost Sunday
Some five and twenty years, and then we masked. twenty five
COUSIN 1.5.44
'Tis more, 'tis more. His son is elder, sir. older than that
His son is thirty.
CAPULET Will you tell me that? 1.5.46
His son was but a ward two years ago. child
ROMEO [seeing Juliet; to a Servant2
] 1.5.48
What lady's that, which doth enrich the hand hold the hand
Of yonder knight? that gentleman
[SERVANT 1.5.50
I know not, sir.]2 [not in 1]
ROMEO 1.5.51
O, she doth teach the torches to burn bright!
It seems she hangs upon the cheek of night
Like1
 a rich jewel in an Ethiope's ear, as2
, Ethiopian's
Beauty too rich for use, for earth too dear! everyday use
So shows a snowy dove trooping with crows, appears, white, among
As yonder lady o'er her fellows shows. that, stands out 1.5.56
The measure done, I'll watch her place of stand, dance, where she goes
And, touching hers, make blessèd my rude hand. touching her hand, rough
Did my heart love till now? Forswear it, sight, before, deny it, eyes
For I ne'er saw true beauty till this night.
TYBALT [aside] 1.5.61
This, by his voice, should be a Montague! must
[to Page] Fetch me my rapier, boy. [Page exits] sword
 What, dares the slave scumbag
Come hither, covered with an antic face, here, mask
To fleer and scorn at our solemnity? sneer, festivity
Now, by the stock and honor of my kin, family
To strike him dead, I hold it not a sin! [starts to go]
CAPULET 1.5.68
Why, how now, kinsman! Wherefore storm you so? hello, why so angry
TYBALT 1.5.69
Uncle, this is a Montague, our foe,
A villain that is hither come in spite came here, to spite and
To scorn at our solemnity this night! festivity
CAPULET 1.5.72
Young Romeo is it?
TYBALT 'Tis he, that villain Romeo. 1.5.73
CAPULET 1.5.74
Content thee, gentle coz. Let him alone. calm down, nephew
He1
 bears him like a portly gentleman, behaves like, dignified
And, to say truth, Verona brags of him
To be a virtuous and well-governed youth. well-behaved
I would not for the wealth of all the town
Here in my house do him disparagement. disrespect him
Therefore be patient. Take no note of him. ignore him 1.5.80
It is my will, the which if thou respect, wish
Show a fair presence and put off these frowns, pleasant face
An ill-beseeming semblance for a feast. inappropriate expression
TYBALT 1.5.84
It fits, when such a villain is a guest.
I'll not endure him!
CAPULET He shall be endured! 1.5.86
What, goodman boy! I say, he shall! Go to! go away
Am I the master here, or you? Go to!
You'll not endure him! God shall mend my soul! save my soul
You'll make a mutiny among my guests? riot
You will set cock-a-hoop? You'll be the man? show off
TYBALT 1.5.92
Why, uncle, 'tis a shame!
CAPULET Go to, go to! 1.5.93
You are a saucy boy! Is't so, indeed? disrespectful
This trick may chance to scathe you, I know what! stunt, get you trouble, I tell you
You must contrary me? Marry, 'tis time— you'll cross me
[to dancing Guests] Well said, my hearts! done, dears
[to Tybalt] You are a princox! Go, cocky boy
Be quiet, or—
[to Servants] More light, more light! torches
[to Tybalt] For shame!
I'll make you quiet!
[going to dancing Guests] What, cheerly, my hearts! wonderful, my dears
TYBALT [aside] 1.5.100
Patience perforce with wilful choler meeting forced on me by his rage
Makes my flesh tremble in their different greeting. me tremble with anger
I will withdraw, but this intrusion shall, go
Now seeming sweet, convert to bitt'rest gall. [exits] okay, bitterness
ROMEO [taking Juliet's hand] (a sonnet starts here) 1.5.104
If I profane with my unworthiest2
 hand defile, unworthy1
This holy shrine, the gentle sin2
 is this: fine+
My lips, two blushing pilgrims, ready stand
To smooth that rough touch with a tender kiss.
JULIET 1.5.108
Good pilgrim, you do wrong your hand too much,
Which mannerly devotion shows in this,
For saints have hands that pilgrims' hands do touch, statues of saints
And palm to palm is holy palmers' kiss. shaking hands, pilgrims'
ROMEO 1.5.112
Have not saints lips, and holy palmers too? pilgrims
JULIET 1.5.113
Ay, pilgrim, lips that they must use in prayer.
ROMEO 1.5.114
O, then dear saint, let lips do what hands do;
They pray: Grant2
 thou, lest faith turn to despair. yield1
, grant me a kiss, else
JULIET 1.5.116
Saints do not move, though grant for prayers' sake. they do grant prayers
ROMEO 1.5.117
Then move not while my prayer's effect I take. [kisses her]
Thus from my lips, by thine, my sin is purged. washed away
JULIET 1.5.119
Then have my lips the sin that they have took. my lips now have your sin
ROMEO 1.5.120
Sin from my lips? O, trespass sweetly urged! so sweetly you tell me I sinned
Give me my sin again. [kisses her] give back
JULIET You kiss by th' book. properly 1.5.122
NURSE 1.5.123
Madam, your mother craves a word with you.
[Juliet goes]
ROMEO [to Nurse] 1.5.124
What is her mother? who
NURSE Marry, bachelor, young sir 1.5.125
Her mother is the lady of the house,
And a good lady, and a wise and virtuous.
I nursed her daughter that you talked withal. with
I tell you, he that can lay hold of her win her
Shall have the chinks. [moves away] money
ROMEO [aside] Is she a Capulet? 1.5.131
O dear account! My life is my foe's debt. costly, in debt to my foe
BENVOLIO [comes to Romeo] 1.5.133
Away, be gone! The sport is at the best! let's go, party, its peak (proverb)
ROMEO 1.5.134
Ay, so I fear. The more is my unrest. uneasiness
[All start to exit but Juliet & Nurse]
CAPULET 1.5.135
Nay, gentlemen, prepare not to be gone,
We have a trifling foolish banquet towards— desert soon
Is it e'en so? Why then, I thank you all.
I thank you, honest gentlemen. Good night.—
More torches here!—Come on, then let's to bed.— bring more, go to bed
Ah, sirrah, by my fay, it waxes late. servant, faith, it's getting late
I'll to my rest. [exit] go rest
JULIET 1.5.142
Come hither, Nurse. What is yond gentleman? here, who is that
NURSE 1.5.143
The son and heir of old Tiberio. 
JULIET 1.5.144
What's he that now is going out of door? who
NURSE 1.5.145
Marry, that, I think, be young Petruchio. well
JULIET 1.5.146
What's he that follows there1
, that would not dance? here2
NURSE 1.5.147
I know not.
JULIET 1.5.148
Go ask his name. [Nurse goes]
[aside] If he be married,
My grave is like to be my wedding bed!
NURSE [returning] 1.5.150
His name is Romeo, and a Montague,
The only son of your great enemy!
JULIET 1.5.152
My only love sprung from my only hate!
Too early seen unknown, and known too late!
Prodigious birth of love it is to me, wonderful and ominous
That I must love a loathed enemy.
NURSE 1.5.156
What's this? What's this?
JULIET A rhyme I learned even now 1.5.157
Of one I danced withal. from someone, with
LADY CAPULET1
 [offstage] Juliet!
NURSE Anon, anon. in a minute 1.5.159
Come, let's away. The strangers all are gone. let's go, guests
[They exit]
ACT 2, PROLOGUE
CHORUS 2.0.1
Now old desire doth in his deathbed lie,
And young affection gapes to be his heir. new love, desires
That fair for which love groaned for and would die, beautiful woman
With tender Juliet matched3
, is now not fair. compared, beautiful
Now Romeo is beloved and loves again, 2.0.5
Alike betwitchèd by the charm of looks, enchanted, gazing
But to his foe supposed he must complain, alleged foe, beg for favor
And she steal love's sweet bait from fearful hooks. must steal, dangerous
Being held a foe, he may not have access regarded as
To breathe such vows as lovers use to swear; lovers swear 2.0.10
And she as much in love, her means much less has even less opportunity
To meet her new belovèd anywhere.
But passion lends them power, time means, to meet, gives opportunities
Temp'ring extremities with extreme sweet. moderating their troubles
ACT 2, SCENE 1
[Outside the Capulet house, same night. ROMEO]
ROMEO 2.1.1
Can I go forward when my heart is here? walk away
Turn back, dull earth, and find thy center out. weary body, follow your heart
[exits]
[BENVOLIO & MERCUTIO enter]
BENVOLIO 2.1.3
Romeo! My cousin Romeo! [Romeo!]2 
MERCUTIO He is wise, 2.1.4
And, on my life, hath stol'n him home to bed.
BENVOLIO 2.1.6
He ran this way and leaped this orchard wall. garden fence
Call, good Mercutio. call him
MERCUTIO Nay, I'll conjure too. 2.1.8
Romeo! Humors! Madman! Passion! Lover! moody one
Appear thou in the likeness of a sigh! form
Speak but one rhyme and I am satisfied.
Cry but "Ay me!" Pronounce1
 but "love" and "dove"1
.
Speak to my gossip Venus one fair word, gossipy lady
One nickname for her purblind son and heir1
, blind 2.1.15
Young Abraham Cupid, he that shot so true2
cheating, trim1
: straight
When King Cophetua loved the beggar-maid!—
He heareth not, he stirreth not, he moveth not.
The ape is dead, and I must conjure him.— monkey is playing dead
I conjure thee by Rosaline's bright eyes, 2.1.20
By her high forehead and her scarlet lip,
By her fine foot, straight leg, and quivering thigh,
And the demesnes that there adjacent lie, "di·máins": region between (bawdy)
That in thy likeness thou appear to us! flesh and blood
BENVOLIO 2.1.25
And if he hear thee, thou wilt anger him!
MERCUTIO 2.1.26
This cannot anger him. 'Twould anger him
To raise a spirit in his mistress' circle (bawdy)
Of some strange nature, letting it there stand
Till she had laid it and conjured it down. cast a spell and laid it down
That were some spite! My invocation would provoke him, spell
Is fair and honest. In his mistress' name,
I conjure only but to raise up him. (bawdy)
BENVOLIO 2.1.33
Come, he hath hid himself among these trees
To be consorted with the humorous night. commune, moody
Blind is his love and best befits the dark.
MERCUTIO 2.1.36
If love be blind, love cannot hit the mark. target
Now will he sit under a medlar tree a fruit of suggestive shape
And wish his mistress were that kind of fruit
As maids call medlars when they laugh alone.— snicker
O, Romeo, that she were, O, that she were 2.1.40
An open-arse and thou a pop'rin pear! medlar, long pear
Romeo, good night.—I'll to my truckle2
-bed. trundle1
: cot
This field-bed is too cold for me to sleep. camping outdoors
Come, shall we go?
BENVOLIO Go then, for 'tis in vain useless 2.1.45
To seek him here that means not to be found.
[They exit]
ACT 2, SCENE 2
[Outside Juliet's balcony. ROMEO]
ROMEO 2.2.1
He jests at scars that never felt a wound. teases me for pains he's never felt
[JULIET enters at window]
But soft, what light through yonder window breaks? wait, that, shines
It is the east, and Juliet is the sun.
Arise, fair sun, and kill the envious moon, beautiful
Who is already sick and pale with grief 2.2.5
That thou her maid art far more fair than she. servant
Be not her maid, since she is envious,
Her vestal livery is but sick2
 and green, virgin's uniform, pale1
And none but fools do wear it. Cast it off. jesters, take them off
It is my lady. O, it is my love! 2.2.10
O, that she knew she were! if only she knew
She speaks, yet she says nothing. What of that? I cannot hear
Her eye discourses; I will answer it. speaks to me
I am too bold. 'Tis not to me she speaks. presumptuous
Two of the fairest stars in all the heaven, 2.2.15
Having some business, do1
 entreat her eyes have begged
To twinkle in their spheres till they return. orbits
What if her eyes were there, they in her head?
The brightness of her cheek would shame those stars, outshine 2.2.20
As daylight doth a lamp. Her eyes1
 in heaven eye2
Would through the airy region stream so bright sky, shine
That birds would sing and think it were not night.
See, how she leans her cheek upon her hand! 2.2.25
O, that I were a glove upon that hand, I wish I were
That I might touch that cheek!
JULIET Ay me! 2.2.27
ROMEO She speaks. 2.2.28
O, speak again, bright angel, for thou art
As glorious to this night, being o'er my head
As is a wingèd messenger of heaven
Unto the white-upturned wondering eyes awe-struck
Of mortals that fall back to gaze on him
When he bestrides the lazy puffing clouds mounts
And sails upon the bosom of the air.
JULIET 2.2.36
O Romeo, Romeo, wherefore art thou Romeo? why must you be "Romeo"
Deny thy father and refuse thy name.
Or, if thou wilt not, be but sworn my love, just swear to be my love
And I'll no longer be a Capulet.
ROMEO 2.2.40
Shall I hear more, or shall I speak at this?
JULIET 2.2.41
'Tis but thy name that is my2
 enemy. only, mine1
Thou art thyself, though not a Montague. you would still be yourself if
What's Montague? It is nor hand, nor foot,
Nor arm, nor face, nor any other part1
Belonging to a man.2
 O, be some other name!1
 2.2.45
What's in a name? That which we call a rose
By any other name1
 would smell as sweet. word2
So Romeo would, were he not Romeo called,
Retain that dear perfection which he owes owns
Without that title. Romeo, doff thy name, discard 2.2.50
And for that1
 name, which is no part of thee, in exchange for, thy2
Take all myself. take all of me
ROMEO [to her] I take thee at they word. 2.2.53
Call me but Love, and I'll be new baptized; re-baptized with a new name
Henceforth I never will be Romeo. from now on
JULIET 2.2.56
What man art thou that thus bescreened in night is hidden
So stumblest on my counsel? eavesdropping on my secrets
ROMEO By a name 2.2.58
I know not how to tell thee who I am.
My name, dear saint, is hateful to myself, 
Because it is an enemy to thee.
Had I it written, I would tear the word.
JULIET 2.2.63
My ears have not yet drunk a hundred words
Of thy tongue's utterance1
, yet I know the sound. uttering2
Art thou not Romeo and a Montague?
ROMEO 2.2.66
Neither, fair saint1
, if either thee dislike. maid2
JULIET 2.2.67
How came'st thou hither, tell me, and wherefore? here, why
The orchard walls are high and hard to climb,
And the place death, considering who thou art,
If any of my kinsmen find thee here. family
ROMEO 2.2.71
With love's light wings did I o'er-perch these walls, fly over
For stony limits cannot hold love out,
And what love can do, that dares love attempt. love will do what it dares
Therefore thy kinsmen are no stop to me. family
JULIET 2.2.75
If they do see2
 thee, they will murder thee! find1
ROMEO 2.2.76
Alack, there lies more peril in thine eye2
danger, eyes1
Than twenty of their swords! Look thou but sweet, upon me sweetly
And I am proof against their enmity. armored, hostility
JULIET 2.2.79
I would not for the world they saw2
 thee here. find1
: want them to see you here
ROMEO 2.2.80
I have night's cloak to hide me from their eyes2
, sight1
And but thou love me, let them find me here. if you do not love me
My life were better ended by their hate
Than death proroguèd, wanting of thy love. postponed, without your love
JULIET 2.2.84
By whose direction found'st thou out this place?
ROMEO 2.2.85
By love, who first did prompt me to inquire. seek you
He lent me counsel and I lent him eyes. advice
I am no pilot, yet wert thou as far navigator
As that vast shore washed1
 with the farthest sea,
I would adventure for such merchandise. treasure
JULIET 2.2.90
Thou know'st the mask of night is on my face,
Else would a maiden blush bepaint my cheek girlish, color
For that which thou hast heard me speak tonight.
Fain would I dwell on form; fain, fain deny gladly, follow formalities
What I have spoke. But farewell compliment! etiquette
Dost thou love me? I know thou wilt say "Ay," 2.2.95
And I will take thy word. Yet if thou swear'st,
Thou mayst prove false. At lovers' perjuries, you may be lying, lies
They say, Jove laughs. O gentle Romeo, the god Jupiter
If thou dost love, pronounce it faithfully.
Or if thou think'st I am too quickly won, 2.2.100
I'll frown and be perverse and say thee nay stubborn, tell you no
So thou wilt woo; but else not for the world. pursue me, otherwise
In truth, fair Montague, I am too fond, too affectionate
And therefore thou mayst think my b'havior2
 light, havior1
: I'm not serious
But trust me, gentleman, I'll prove more true faithful 2.2.105
Than those that have more1
 coying to be strange. who play hard-to-get
I should have been more strange, I must confess, aloof
But that thou overheard'st, ere I was 'ware, before I was aware
My true-love passion. Therefore pardon me, 2.2.109
And not impute this yielding to light love, misinterpret, shallow/unchaste
Which the dark night hath so discoverèd.
ROMEO 2.2.112
Lady, by yonder blessèd moon I swear1
that, vow2
That tips with silver all these fruit-tree tops— shines
JULIET 2.2.114
O, swear not by the moon, the inconstant moon, ever-changing
That monthly changes in her circled1
 orb, orbit
Lest that thy love prove likewise variable. unless, inconsistent
ROMEO 2.2.117
What shall I swear by?
JULIET Do not swear at all. 2.2.118
Or, if thou wilt, swear by thy gracious self,
Which is the god of my idolatry, devotion
And I'll believe thee.
ROMEO If my heart's dear love— 2.2.122
JULIET 2.2.123
Well, do not swear. Although I joy in thee, enjoy seeing you
I have no joy of this contract tonight. these vows
It is too rash, too unadvised, too sudden, 2.2.125
Too like the lightning, which doth cease to be
Ere one can say "It lightens." Sweet, good night! before, sweetheart
This bud of love, by summer's ripening breath,
May prove a beauteous flower when next we meet. become
Good night, good night! As sweet repose and rest sleep 2.2.130
Come to thy heart as that within my breast! heart
ROMEO 2.2.132
O, wilt thou leave me so unsatisfied?
JULIET 2.2.133
What satisfaction canst thou have tonight?
ROMEO 2.2.134
Th' exchange of thy love's faithful vow for mine.
JULIET 2.2.135
I gave thee mine before thou didst request it,
And yet I would it were to give again. I wish it were still mine
ROMEO 2.2.137
Wouldst thou withdraw it? For what purpose, love?
JULIET 2.2.138
But to be frank and give it thee again. just to be lavish
And yet I wish but for the thing I have.
My bounty is as boundless as the sea, gifts
My love as deep. The more I give to thee,
The more I have, for both are infinite.
NURSE [inside, calls for Juliet]
JULIET 2.2.143
I hear some noise within. Dear love, adieu! inside, goodbye
[to her] Anon, good Nurse! in a minute
[to him] Sweet Montague, be true.
Stay but a little; I will come again. [goes in] wait, just, back
ROMEO 2.2.146
O blessèd, blessèd night! I am afeard, afraid
Being in night, all this is but a dream,
Too flattering-sweet to be substantial. wonderfully, real
JULIET [comes out again] 2.2.149
Three words, dear Romeo, and good night indeed.
If that thy bent of love be honorable, your intentions
Thy purpose marriage, send me word tomorrow
By one that I'll procure to come to thee, someone, arrange
Where and what time thou wilt perform the rite, wedding
And all my fortunes at thy foot I'll lay life
And follow thee my lord throughout the world. husband
NURSE [inside] 2.2.156
Madam!
JULIET 2.2.157
[to her] I come, anon!
[to him] But if thou mean'st not well,
I do beseech thee— beg
NURSE [inside] Madam! 2.2.159
JULIET [to her] By and by I come! soon 2.2.160
[to him] To cease thy suit+
 and leave me to my grief. courtship / strife2
Tomorrow will I send. send my messenger
ROMEO So thrive2
 my soul— strive+
: upon my soul 2.2.163
JULIET 2.2.164
A thousand times good night! [goes in]
ROMEO 2.2.165
A thousand times the worse to want thy light. without
Love goes toward love as schoolboys from their books,
But love from love, toward school with heavy looks. reluctant
JULIET [comes out again] 2.2.169
Hist! Romeo, hist! [aside] O, for a falc'ner's voice psst, if only I had
To lure this tassel-gentle back again! noble hawk
Bondage is hoarse, and may not speak aloud, my father is strict, I may, loud
Else would I tear the cave where Echo lies, the nymph Echo
And make her airy tongue more hoarse than mine1
voice
With repetition of "My Romeo!" echoing
ROMEO [aside] 2.2.175
It is my soul that calls upon my name!
How silver-sweet sound lovers' tongues by night, voices
Like softest music to attending ears! listening
JULIET 2.2.178
Romeo!
ROMEO My dear4
? madame1
/niece2
/nyas+
 2.2.179
JULIET What o'clock tomorrow time 2.2.180
Shall I send to thee?
ROMEO By the hour of nine. 2.2.182
JULIET 2.2.183
I will not fail. 'Tis twenty years till then.
I have forgot why I did call thee back.
ROMEO 2.2.185
Let me stand here till thou remember it.
JULIET 2.2.186
I shall forget, to have thee still stand there,
Remembering how I love thy company.
ROMEO 2.2.188
And I'll still stay, to have thee still forget,
Forgetting any other home but this.
JULIET 2.2.190
'Tis almost morning. I would have thee gone,
And yet no further than a wanton's bird, spoiled girl's
Who1
 lets it hop a little from her1
 hand, that2
, his2
Like a poor prisoner in his twisted gyves, chains
And with a silk1
 thread plucks it back again, silken2
So loving-jealous of his liberty.
ROMEO 2.2.196
I would I were thy bird. wish I were
JULIET Sweet, so would I. sweetheart 2.2.197
Yet I should kill thee with much cherishing. 
Good night, good night! Parting is such sweet sorrow
That I shall say good night till it be morrow. [exits] morning
ROMEO1
2.2.202
Sleep dwell upon thine eyes, peace in thy breast! rest, heart
Would I were sleep and peace, so sweet to rest! if, rest there
Hence will I to my ghostly Friar's close cell, away, go to, spiritual, chamber
His help to crave, and my dear hap to tell. [exits] ask for, fortune
ACT 2, SCENE 3
[St. Peter's Church, dawn. FRIAR LAWRENCE with basket]
FRIAR 2.3.1
The grey-eyed morn smiles on the frowning night,
Check'ring the eastern clouds with streaks of light,
And fleckled darkness like a drunkard reels dappled, staggers
From forth day's path and Titan's fiery1
 wheels. out of the way of, burning2
: sun-chariot
Now, ere the sun advance his burning eye, before, raises 2.3.5
The day to cheer and night's dank dew to dry,
I must up-fill this osier cage of ours basket
With baleful weeds and precious-juiced flowers. harmful
The earth that's nature's mother is her tomb;
What is her burying grave, that is her womb; is also 2.3.10
And from her womb children of divers kind diverse plants
We sucking on her natural bosom find
Many for many virtues excellent, many plants have healing powers
None but for some and yet all different. all good for something
O, mickle is the powerful grace that lies great, healing power 2.3.15
In plants, herbs, stones, and their true qualities. extracts
For naught so vile that on the earth doth live nothing is so evil
But to the earth some special good doth give, humankind
Nor aught so good but, strained from that fair use, anything, that cannot be
Revolts from true birth, stumbling on abuse. abused for harm
Virtue itself turns vice, being misapplied, becomes vice when misapplied
And vice sometimes by action dignified. can be good if the result is good
[examining a flower]
Within the infant rind of this weak flower frail
Poison hath residence and medicine power: 2.3.24
For this, being smelt, with that part cheers each part; makes you feel better
Being tasted, slays1
 all senses with the heart. stays2
: kills you
Two such opposéd kings encamp them still enemy, always
In man as well as herbs, grace and rude will; good and evil
And where the worser is predominant, evil 2.3.30
Full soon the canker death eats up that plant. infection of
ROMEO [enter] 2.3.32
Good morrow, Father. morning
FRIAR Benedicité! bless you 2.3.33
What early tongue so sweet saluteth me? hails
Young son, it argues a distempered head suggests, disturbed mind
So soon to bid good morrow to thy bed. leaving your bed so early
Care keeps his watch in every old man's eye, worry stays on guard
And where care lodges, sleep will never lie; worry stays, lie down
But where unbruisèd youth with unstuffed brain trouble-free, clear minds
Doth couch his limbs, there golden sleep doth reign. rest 2.3.40
Therefore thy earliness doth me assure
Thou art up-roused by some distemperature; something upsetting
Or if not so, then here I hit it right:
Our Romeo hath not been in bed tonight. last night 
ROMEO 2.3.46
That last is true. The sweeter rest was mine. I had an even sweeter rest
FRIAR 2.3.47
God pardon sin! Wast thou with Rosaline?
ROMEO 2.3.48
With Rosaline, my ghostly Father? No! spiritual
I have forgot that name and that name's woe.
FRIAR 2.3.50
That's my good son. But where hast thou been then?
ROMEO 2.3.52
I'll tell thee ere thou ask it me again. before
I have been feasting with mine enemy,
Where on a sudden one hath wounded me suddenly
That's by me wounded. Both our remedies who I had wounded, cures
Within thy help and holy physic lies. spiritual remedy
I bear no hatred, blessèd man, for lo, look
My intercession likewise steads my foe. my plea also helps my foe (Juliet)
FRIAR 2.3.59
Be plain, good son, and homely in thy drift. simple, speech
Riddling confession finds but riddling shrift. confessing in riddles, absolution
ROMEO 2.3.61
Then plainly know my heart's dear love is set
On the fair daughter of rich Capulet.
As mine on hers, so hers is set on mine,
And all combined, save what thou must combine we are combined except
By holy marriage. When and where and how
We met, we wooed and made exchange of vow,
I'll tell thee as we pass, but this I pray, walk
That thou consent to marry us today.
FRIAR 2.3.69
Holy Saint Francis, what a change is here!
Is Rosaline, whom1
 thou didst love so dear, that2
So soon forsaken? Young men's love then lies forgotten
Not truly in their hearts, but in their eyes.
Jesu Maria, what a deal of brine a lot of salt water
Hath washed thy sallow cheeks for Rosaline! yellow
How much salt water thrown2
 away in waste cast1
 2.3.75
To season love, that of it doth not taste! to season a love you did not taste
The sun not yet thy sighs from heaven clears, dried the fog of your sighs
Thy old groans ring yet1
 in mine2
 ancient ears. yet ringing2
, my1
Lo, here upon thy cheek the stain doth sit look
Of an old tear that is not washed off yet. 2.3.80
If e'er thou wast thyself and these woes thine,
Thou and these woes were all for Rosaline.
And art thou changed? Pronounce this sentence then: repeat this saying
"Women may fall when there's no strength in men." fall from grace when
ROMEO men have no strength
Thou chide'st me oft for loving Rosaline. scolded me often 2.3.86
FRIAR 2.3.87
For doting, not for loving, pupil mine.
ROMEO 2.3.88
And bade'st me bury love. told
FRIAR Not in a grave 2.3.89
To lay one in, another out to have. and take another out
ROMEO 2.3.91
I pray thee, chide me not. Her I love now please don't scold me, the girl
Doth grace for grace and love for love allow. returns my joy and love
The other did not so. 
FRIAR O, she knew well 2.3.94
Thy love did read by rote and1
 could not spell. recite from memory, that2
, read
But come, young waverer, come, go with me.
In one respect I'll thy assistant be, for one reason I'll help you
For this alliance may so happy prove marriage
To turn your households' rancor to pure love. families' hatred
ROMEO 2.3.100
O, let us hence! I stand on sudden haste! go, I cannot wait
FRIAR 2.3.101
Wisely and slow. They stumble that run fast.
[They exit]
ACT 2, SCENE 4
[A street, noon. BENVOLIO & MERCUTIO]
MERCUTIO 2.4.1
Where the devil should this Romeo be?
Came he not home tonight? last night
BENVOLIO 2.4.3
Not to his father's. I spoke with his man. manservant
MERCUTIO 2.4.4
Ah1
, that same pale hard-hearted wench, that Rosaline, why2
Torments him so, that he will sure run mad.
BENVOLIO 2.4.7
Tybalt, the kinsman of1
 old Capulet, nephew, to2
Hath sent a letter to his father's house. Romeo's
MERCUTIO 2.4.9
A challenge, on my life. I bet my life it's a challenge to fight
BENVOLIO 2.4.10
Romeo will answer it. accept it
MERCUTIO 2.4.11
Any man that can write may answer a letter.
BENVOLIO 2.4.12
Nay, he will answer the letter's master, Tybalt
how he dares, being dared. accepting the dare
MERCUTIO 2.4.14
Alas poor Romeo, he is already dead, stabbed with
a white wench's black eye, shot1
 through the ear with woman's, run2
: stabbed
a love-song, the very pin of his heart cleft with bull's-eye, cut
the blind bow-boy's butt-shaft. And is he a man Cupid's arrow (bawdy pun)
to encounter Tybalt? fight
BENVOLIO 2.4.19
Why, what is Tybalt? what's so scary about Tybalt
MERCUTIO 2.4.20
More than Prince of Cats [I can tell you]1
. (a cat named Tybalt in a popular story)
O, he's the courageous captain of compliments. fencing etiquette
He fights as you sing prick-song, keeps time, harmony in a duet
distance, and proportion. He rests his minim rests, short
one, two, and the third in your bosom; the very thrust in your chest
butcher of a silk button; a duelist, a duelist, silk shirt, swordsman
a gentleman of the very first house best fencing school
of the first and second cause. Ah, the immortal well trained in fencing codes
passado! The punto reverso! The hay!— forward thrust, backhand, hit
BENVOLIO 2.4.28
The what?
MERCUTIO 2.4.29
The pox of such antic, lisping, may the plague kill, silly, Spanish-accented
affecting fantasticoes1
, these new affected showoffs
tuners of accents: "By Jesu, a very good blade! A users of catch-phrases
very tall man! A very good whore!" Why, is not this brave
a lamentable thing, grandsire, that we should be thus sorry, old sir
afflicted with these strange flies, these fashion-mongers, foreign parasites
these pardon-me's, who stand so much on the new form, trends/bench
that they cannot sit at ease on the old bench?
O, their bones, their bones!
[ROMEO enters]
BENVOLIO 2.4.38
Here comes Romeo, [here comes Romeo]2
.
[not in 1]
MERCUTIO 2.4.39
Without his roe, like a dried herring. O flesh, fish eggs (sexually spent)
flesh, how art thou fishified! Now is he for the
numbers that Petrarch flowed in. Laura to verses, wrote, compared to
his lady was a kitchen-wench (marry, she although
had a better love to be-rhyme her), Dido lover, write her in poetry
a dowdy, Cleopatra a gipsy, Helen and Hero was shabby
hildings and harlots, Thisbe a grey eye or so, but loose women
not to the purpose.—Signor Romeo, bonjour! nothing worth mentioning
There's a French salutation to your French slop. pants
You gave us the counterfeit fairly last night. a fake
ROMEO 2.4.48
Good morrow to you both. What counterfeit did I give you? day
MERCUTIO 2.4.50
The slip, sir, the slip. Can you not conceive? counterfeit money, follow me
ROMEO 2.4.51
Pardon, good Mercutio, my business was great, and important
in such a case as mine a man may strain courtesy. bend the rules of
MERCUTIO 2.4.54
That's as much as to say such a case as yours
constrains a man to bow in the hams. forces, bend from bowed-legs
ROMEO 2.4.56
Meaning, to curtsy.
MERCUTIO 2.4.57
Thou hast most kindly hit it. now you got it
ROMEO 2.4.58
A most courteous exposition. explanation
MERCUTIO 2.4.59
Nay, I am the very pink of courtesy. perfect example
ROMEO 2.4.60
"Pink" for flower? pink like a flower
MERCUTIO 2.4.61
Right.
ROMEO 2.4.62
[Why,]2
 then is my pump well flowered! [not in 1], shoe, (cut with "pinking" shears)
MERCUTIO 2.4.63
Sure wit! Follow me this jest now till thou hast worn good, joke
out thy pump, that when the single sole of it is worn, shoe
the jest may remain, after the wearing, solely singular! outlast it
ROMEO 2.4.67
O single-soled jest, solely singular for the singleness! thin-soled joke
MERCUTIO 2.4.69
Come between us, good Benvolio. My wits faint. stop us, my wit is tired
ROMEO 2.4.71
Switch and spurs, switch and spurs, or I'll cry a match! bring it on, declare victory
MERCUTIO 2.4.73
Nay, if our2
 wits run the wild-goose chase, I am done, thy1
for thou hast more of the wild goose in one of thy wits 
than, I am sure, I have in my whole five. Was I with
you there for the goose? goose joke
ROMEO 2.4.77
Thou wast never with me for anything when thou wast
not there for the goose! as a fool
MERCUTIO 2.4.79
I will bite thee by the ear for that jest! on
ROMEO 2.4.80
Nay, good goose, bite not!
MERCUTIO 2.4.81
Thy wit is a very bitter sweeting; it is a most sharp sauce. apple
ROMEO 2.4.83
And is it not [then]2
 well served into a sweet goose? isn't a sharp sauce served with
MERCUTIO 2.4.85
O, here's a wit of cheveril, that stretches from an baby goat leather
inch narrow to an ell broad! forty five inches
ROMEO 2.4.87
I stretch it out for that word "broad", which added
to the goose, proves thee far and wide a broad goose! a big fat goose
MERCUTIO 2.4.90
Why, is not this better now than groaning for love? Now art well
thou sociable, now art thou Romeo, now art thou what thou
art, by art as well as by nature. For this drivelling love stupid-talking
is like a great natural that runs lolling up idiot, with his tongue out
and down to hide his bauble in a hole! looking for a hole to hide his toy in
BENVOLIO 2.4.96
Stop there, [stop there]2
! [not in 1]
MERCUTIO 2.4.97
Thou desire'st me to stop in my tale against the hair. against my wish
BENVOLIO 2.4.99
Thou wouldst else have made thy tale large2
! otherwise you'd, too long1
 (bawdy)
MERCUTIO 2.4.100
O, thou art deceived. I would have made it short, for I
was come to the whole depth of my tale, taken it as far as I could (bawdy)
and meant indeed to occupy the argument no longer! end it there
[NURSE & PETER enter]
ROMEO [sees Nurse; to Mercutio] 2.4.103
Here's goodly gear! a huge outfit (also bawdy)
MERCUTIO1
 [making fun of her clothes] ROMEO2
 2.4.104
A sail, a sail!
BENVOLIO1 MERCUTIO2
 2.4.105
Two, two: a shirt and a smock. man's shirt, woman's smock
NURSE 2.4.106
Peter!
PETER 2.4.107
Anon! coming
NURSE 2.4.108
My fan, Peter.
MERCUTIO 2.4.109
Good Peter, to hide her face, for her fan's the fairer face. prettier
NURSE 2.4.111
God ye good morrow, gentlemen. morning
MERCUTIO 2.4.112
God ye good e'en, fair gentlewoman. afternoon
NURSE 2.4.113
Is it good e'en? afternoon
MERCUTIO 2.4.114
'Tis no less, I tell ye2
, for the bawdy hand of the you1
, vulgar
dial is now upon the prick of noon. erect at 
NURSE 2.4.116
Out upon you! What a man are you? what kind of man
ROMEO 2.4.117
One, gentlewoman, that God hath made for himself to mar. injure
NURSE 2.4.119
By my troth, it is well said. "For himself to mar," truth
quoth he? Gentlemen, can any of you tell me where I said
may find [the]2
 young Romeo? [not in 1]
ROMEO 2.4.122
I can tell you, but young Romeo will be older when you
have found him than he was when you sought him. I am
the youngest of that name, for fault of a worse. lack
NURSE 2.4.126
You say well. well put
MERCUTIO 2.4.127
Yea, is the worst well? Very well took, i' faith; taken, indeed
wisely, wisely. very wise
NURSE 2.4.129
If you be he, sir, I desire some confidence with ye1
. you2
BENVOLIO [making fun of her wrong word for "conference"] 2.4.131
She will "indite" him to some supper!
MERCUTIO 2.4.132
A bawd, a bawd, a bawd! So ho! whore/hare, (a hunting call)
ROMEO 2.4.133
What hast thou found?
MERCUTIO 2.4.134
No hare, sir, unless a hare, sir, in a Lenten pie, rabbit/whore, pie for Lent
that is something stale and hoar ere it be spent. [sings] moldy, before, done
 "An old hare hoar, grey
 And an old hare hoar,
 Is very good meat in Lent;
 But a hare that is hoar
 Is too much for a score, not worth paying for
 When it hoars ere it be spent." molds, before, eaten
Romeo, will you come to your father's?
We'll to dinner thither. go to, there
ROMEO 2.4.144
I will follow you.
MERCUTIO 2.4.145
Farewell ancient lady, farewell [sings] "lady, lady, lady."
[Mercutio & Benvolio exit]
NURSE 2.4.147
I pray you, sir, what saucy merchant disrespectful fellow
was this that was so full of his ropery? dirty jokes
ROMEO 2.4.149
A gentleman, Nurse, that loves to hear himself talk and will
speak more in a minute than he will stand to in a month. do
NURSE 2.4.152
If1
 he speak anything against me, I'll take him down, and2
if1
 he were lustier than he is, and twenty such and2
, and even friskier men
jacks! And if I cannot, I'll find those that shall! men, who will
Scurvy knave! I am none of his flirt-gills! stupid jerk, loose girls
I am none of his skains-mates! cutthroat pals
[to Peter] And thou must stand by too, and just
suffer every knave to use me at his pleasure! allow, jerk, make fun of me
PETER 2.4.159
I saw no man use you at his pleasure. If I had, my
weapon should quickly have been out, I warrant you! I swear
I dare draw as soon as another man, if I see
occasion in a good quarrel, and the law on my side. chance of a good fight
NURSE 2.4.164
Now, afore God, I am so vexed that every part about upset
me quivers. Scurvy knave!
[to Romeo] Pray you, sir, a word. And as I told you,
my young lady bade1
 me inquire you out. What she bid2
: asked me to find you
bade1
 me say, I will keep to myself. But first let me tell bid2
: asked me to say
ye, if you1
 should lead her into1
 a fool's paradise, as they ye2
, in2

say, it were a very gross kind of behavior, as they say,
For the gentlewoman is young, and therefore, if you
should deal double with her, truly it were an ill thing to cheat on, horrible
be offered to any gentlewoman, and very weak dealing! mean trick
ROMEO 2.4.175
Nurse, commend me to thy lady and mistress. give my regards
I protest unto thee— solemnly swear
NURSE 2.4.177
Good heart, and i' faith I will tell her as much.
Lord, Lord, she will be a joyful woman!
ROMEO 2.4.179
What wilt thou tell her, Nurse? Thou dost not mark me. did not listen to me
NURSE 2.4.181
I will tell her, sir, that you do protest, which, as
I take it, is a gentlemanlike offer.
ROMEO 2.4.183
Bid her devise ask her to find
Some means to come to shrift this afternoon, some way, confession
And there she shall at Friar Lawrence' cell chamber
Be shrived and married. give confession
[offers her money] Here is for thy pains.
NURSE 2.4.187
No truly sir, not a penny!
ROMEO 2.4.188
Go to, I say you shall. I insist
NURSE 2.4.189
This afternoon, sir? Well, she shall be there.
ROMEO 2.4.190
And stay, good Nurse, behind the abbey wall. wait, church
Within this hour my man shall be with thee servant
And bring thee cords made like a tackled stair, a rope ladder
Which to the high top-gallant of my joy peak
Must be my convoy in the secret night. path
Farewell, be trusty, and I'll quit thy pains. trustworthy, reward you
Farewell, commend me to thy mistress. give my regards
NURSE 2.4.197
Now God in heaven bless thee! Hark you, sir. listen
ROMEO 2.4.198
What say'st thou, my dear Nurse?
NURSE 2.4.199
Is your man secret? Did you ne'er hear say, able to keep a secret
"Two may keep counsel, putting one away"? a secret, if one's not there
ROMEO 2.4.201
I
+
 warrant thee, my man's as true as steel. I promise you
NURSE 2.4.202
Well, sir, my mistress is the sweetest lady, Lord,
Lord, when 'twas a little prating thing! O, there babbling
is a nobleman in town, one Paris, that would fain gladly
lay knife aboard. But she, good soul, had as lief claim her, would rather
see a toad, a very toad, as see him. I anger her 
sometimes and tell her that Paris is the properer handsomer
man. But I'll warrant you, when I say so, she looks I swear
as pale as any clout in the versal world. Doth not sheet, whole
"rosemary" and "Romeo" begin both with a letter? the same letter
ROMEO 2.4.211
Ay, Nurse, what of that? Both with an R.
NURSE 2.4.212
Ah, mocker, that's the dog's name! you mock me, a dog goes "Rrrr"
R is for the—no, I know it begins with some other
letter—and she hath the prettiest sententious of it, (she means "sentence")
of you and rosemary, that it would do you good to hear it.
ROMEO 2.4.216
Commend me to thy lady. my regards
NURSE 2.4.217
Ay, a thousand times. [Romeo exits]
Peter!
PETER 2.4.218
Anon! coming
NURSE 2.4.219
Before and apace. go ahead, quickly
[They exit]
ACT 2, SCENE 5
[Capulet house. JULIET]
JULIET 2.5.1
The clock struck nine when I did send the2
 Nurse. my1
In half an hour she promised to return.
Perchance she cannot meet him. That's not so. perhaps, find
O, she is lame! Love's heralds should be thoughts, slow, messengers
Which ten times faster glide than the sun's beams, 2.5.5
Driving back shadows over louring hills. gloomy
Therefore do nimble-pinioned doves draw Love, that's why, swift-winged,
And therefore hath the wind-swift Cupid wings. Venus' chariot, swift
Now is the sun upon the highmost hill highest point
Of this day's journey, and from nine till twelve 2.5.10
Is three3
 long hours, yet she is not come.
Had she affections and warm youthful blood, feelings
She would be as swift in motion as a ball.
My words would bandy her to my sweet love, toss
And his to me. toss her back to me 2.5.15
But old folks, many feign as they were dead, act like
Unwieldy, slow, heavy and pale as lead.
[NURSE & PETER enter]
O God, she comes! O honey Nurse, what news?
Hast thou met with him? Send thy man away. servant
NURSE 2.5.20
Peter, stay at the gate. [Peter exits]
JULIET 2.5.21
Now, good sweet Nurse—O Lord, why look'st thou sad?
Though news be sad, yet tell them merrily. if the news is sad, tell it merrily
If good, thou shame'st the music of sweet news are ruining
By playing it to me with so sour a face.
NURSE 2.5.26
I am aweary, give me leave awhile. tired, leave me alone
Fie, how my bones ache! What a jaunt1
 have I [had]1
! oh, jaunce2
: long trip
JULIET 2.5.28
I would thou hadst my bones, and I thy news. wish
Nay, come, I pray thee, speak! Good, good Nurse, speak!
NURSE 2.5.31
Jesu, what haste! Can you not stay awhile? wait
Do you not see that I am out of breath?
JULIET 2.5.33
How art thou out of breath, when thou hast breath
To say to me that thou art out of breath?
The excuse that thou dost make in this delay
Is longer than the tale thou dost excuse. you aren't telling
Is thy news good, or bad? Answer to that!
Say either, and I'll stay the circumstance! wait for the details
Let me be satisfied: is't good or bad?
NURSE 2.5.40
Well, you have made a simple choice! You know not foolish
how to choose a man. Romeo? No, not he! Though
his face be better than any man's, yet his leg excels
all men's, and for a hand and a foot and a body,
though they be not to be talked on, yet they are nothing to talk about
past compare. He is not the flower of courtesy, beyond comparison, model
but I'll warrant him as gentle as a lamb. Go thy ways, I bet he's, along
wench, serve God. What, have you dined at home? girl
JULIET 2.5.49
No, no. But all this did I know before.
What says he of our marriage? What of that?
NURSE 2.5.51
Lord, how my head aches! What a head have I! headache
It beats as it would fall in twenty pieces. break
My back, o' th' other side! O, my back, my back!
Beshrew your heart for sending me about curse, all around
To catch my death with jaunting up and down!
JULIET 2.5.56
I' faith, I am sorry that thou art not well.
Sweet, sweet, sweet Nurse, tell me, what says my love?
NURSE 2.5.59
Your love says, like an honest gentleman, and a courteous,
and a kind, and a handsome, and, I warrant, a virtuous— I believe
Where is your mother?
JULIET 2.5.62
Where is my mother? Why, she is within. inside
Where should she be? How oddly thou repliest! what an odd reply
"Your love says, like an honest gentleman,
'Where is your mother?'"
NURSE O God's lady dear! 2.5.66
Are you so hot? Marry, come up, I trow. impatient, really now
Is this the poultice for my2
 aching bones? medicine, mine1
Henceforward do your messages yourself. from now on
JULIET 2.5.70
Here's such a coil! Come, what says Romeo? such a fuss
NURSE 2.5.71
Have you got leave to go to shrift today? permission, confession
JULIET 2.5.72
I have.
NURSE 2.5.73
Then hie you hence to Friar Lawrence' cell. hurry, away, chamber
There stays a husband to make you a wife! waits
Now comes the wanton blood up in your cheeks; uncontrollable
They'll be in scarlet straight at any news. turn red, immediately
Hie you to church. I must another way hurry, must go
To fetch a ladder, by the which your love
Must climb a bird's nest soon when it is dark. to your room
I am the drudge and toil in your delight, one who works for
But you shall bear the burden soon at night! do the work (bawdy)
Go! I'll to dinner. Hie you to the cell! hurry, friar's chamber
JULIET 2.5.83
Hie to high fortune, honest Nurse. Farewell! bless you with good fortune
[They exit]
ACT 2, SCENE 6
[Church, afternoon. FRIAR & ROMEO]
FRIAR 2.6.1
So smile the heavens upon this holy act, may heaven smile
That after-hours with sorrow chide us not! and not give us sorrow later
ROMEO 2.6.3
Amen, amen! But come what sorrow can, whatever sorrow comes
It cannot countervail the exchange of joy outweigh
That one short minute gives me in her sight.
Do thou but close our hands with holy words, if you'll just join our hands
Then love-devouring death do what he dare.
It is enough I may but call her mine. just
FRIAR 2.6.9
These violent delights have violent ends
And in their triumph die, like fire and powder, at their peak, gunpowder
Which, as they kiss, consume. The sweetest honey are used
Is loathsome in his own deliciousness, can make you sick in its
And in the taste confounds the appetite. when tasted it ruins
Therefore love moderately; long love doth so. that's how love lasts
Too swift arrives as tardy as too slow. makes you as late as those
[JULIET enters]
Here comes the lady. O, so light a foot
Will ne'er wear out the everlasting flint. path 2.6.17
A lover may bestride the gossamers walk on spider-webs
That idles in the wanton summer air, float, playful
And yet not fall, so light is vanity. earthly pleasures
JULIET 2.6.21
Good even to my ghostly confessor. evening, spiritual
FRIAR 2.6.22
Romeo shall thank thee, daughter, for us both.
[Romeo kisses her]
JULIET 2.6.23
As much to him, else is his thanks too much. I'll return as much thanks,
[kisses Romeo back] otherwise he gave to much
ROMEO 2.6.24
Ah, Juliet, if the measure of thy joy scale
Be heaped like mine, and that thy skill be more great
To blazon it, then sweeten with thy breath describe
This neighbor air, and let rich music's4
 tongue nearby, music of your speech
Unfold the imagined happiness that both reveal, unspoken
Receive in either by this dear encounter. we share, meeting
JULIET 2.6.30
Conceit, more rich in matter than in words, imagination, reality
Brags of his substance, not of ornament.
They are but beggars that can count their worth. wealth
But my true love is grown to such excess
I cannot sum up sum of half my wealth. 
FRIAR 2.6.35
Come, come with me, and we will make short work. work quickly
For, by your leaves, you shall not stay alone begging your pardons, cannot
Till Holy Church incorporate two in one. join you two in marriage
[They exit]
ACT 3, SCENE 1
[A street. MERCUTIO, BENVOLIO & Servants]
BENVOLIO 3.1.1
I pray thee, good Mercutio, let's retire. let's go home
The day is hot, the Capulets5
 abroad, Capels are1
: are out
And if we meet we shall not 'scape a brawl, escape
For now these hot days is the mad blood stirring. hot days stir our temper
MERCUTIO 3.1.5
Thou art like one of these2
 fellows that when he enters those1

the confines of a tavern claps me his sword upon the slams
table and says, "God send me no need of thee!"
and by the operation of the second cup, when the 2nd drink takes effect
draws it1
 on the drawer, when indeed him2
, draws his sword on the barkeeper
there is no need.
BENVOLIO 3.1.11
Am I like such a fellow?
MERCUTIO 3.1.12
Come, come, thou art as hot a jack in thy mood as hot-tempered, man
any in Italy, and as soon moved to be moody, and as
soon moody to be moved. angered
BENVOLIO 3.1.15
And what to?
MERCUTIO [pretending he meant "two"] 3.1.16
Nay, and there were two such, we should have oh no, if, two of you
none shortly, for one would kill the other. Thou? soon
Why, thou wilt quarrel with a man that hath a hair
more or a hair less in his beard than thou hast. Thou
wilt quarrel with a man for cracking nuts, having no
other reason but because thou hast hazel eyes. What whose
eye but such an eye would spy out such a quarrel? your, seek
Thy head is as full of quarrels as an egg is full of
meat, and yet thy head hath been beaten as addle as food, scrambled
an egg for quarreling. Thou hast quarreled with a
man for coughing in the street because he hath
wakened thy dog that hath lain asleep in the sun.
Didst thou not fall out with a tailor for wearing his quarrel
new doublet before Easter? With another for tying jacket
his new shoes with old ribbon? And yet thou wilt shoelace
tutor me from quarreling? lecture
BENVOLIO 3.1.32
And I were so apt to quarrel as thou art, any man should if
buy the fee-simple of my life for an hour and a quarter. ownership
MERCUTIO 3.1.35
The fee-simple! O simple!
[TYBALT & other Capulets enter]
BENVOLIO 3.1.36
By my head, here come the Capulets.
MERCUTIO 3.1.37
By my heel, I care not!
TYBALT 3.1.38
[to Capulets] Follow me close, for I will speak to them. 
[to Benvolio & Mercutio]
Gentlemen, good e'en. A word with one of you. afternoon
MERCUTIO 3.1.40
And but one word with one of us? Couple it with
something: make it a word and a blow! something else
TYBALT 3.1.42
You shall find me apt enough to that, sir, happy
and you will give me occasion! if, a reason
MERCUTIO 3.1.44
Could you not take some occasion without giving? make your own reason
TYBALT 3.1.46
Mercutio, thou consort'st with Romeo— hang out with Romeo
MERCUTIO 3.1.47
Consort! What, dost thou make us minstrels? ensemble, musicians
And thou make minstrels of us, look to if
hear nothing but discords. Here's my disagreement/dissonance
fiddlestick! Here's that shall make you dance! (sword)
Zounds, consort! my god
BENVOLIO 3.1.51
We talk here in the public haunt of men. public streets
Either withdraw unto some private place,
Or reason coldly of your grievances, calmly discuss your complaints
Or else depart! Here all eyes gaze on us.
MERCUTIO 3.1.55
Men's eyes were made to look, and let them gaze.
I will not budge for no man's pleasure, I! to please anyone
[ROMEO enters]
TYBALT 3.1.57
Well, peace be with you, sir. Here comes my man.
MERCUTIO 3.1.58
But I'll be hanged, sir, if he wear your livery! damned, manservant's uniform
Marry, go before to field, he'll be your follower! to a dueling field, follow you
Your Worship in that sense may call him "man"! manservant
TYBALT 3.1.61
Romeo! The love2
 I bear thee can afford hate1
: I have so little love for you
No better term than this: Thou art a villain! all I can say is this
ROMEO 3.1.63
Tybalt, the reason that I have to love thee
Doth much excuse the appertaining rage rage you deserve
To such a greeting. Villain am I none. for
Therefore farewell. I see thou know'st me not.
TYBALT 3.1.67
Boy, this shall not excuse the injuries
That thou hast done me. Therefore turn and draw!
ROMEO 3.1.69
I do protest I never injured thee,
But love thee better than thou canst devise imagine
Till thou shalt know the reason of my love. until you learn
And so, good Capulet, which name I tender care for
As dearly as mine2
 own, be satisfied. my5
MERCUTIO 3.1.74
O calm, dishonorable, vile submission! what a
Alla stoccato carries it away! [draws his sword] let the best fencer win
Tybalt, you rat-catcher, will you walk? filthy cat, come here
TYBALT 3.1.76
What wouldst thou have with me?
MERCUTIO 3.1.77
Good King of Cats, nothing but one of your
nine lives that I mean to make bold withal, beat
and as you shall use me hereafter, dry-beat the if you offend, beat
rest of the eight! Will you pluck your sword
out of his pilcher by the ears? Make haste, scabbard, hurry
lest mine be about your ears ere it be out! or else mine will cut off your ears
TYBALT before yours is out
I am for you. [draws his sword] I am ready for you 3.1.84
ROMEO 3.1.85
Gentle Mercutio, put thy rapier up! sword, away
MERCUTIO 3.1.86
Come, sir, your passado! best stroke
[They fight]
ROMEO 3.1.87
Draw, Benvolio, beat down their weapons! disarm them
Gentlemen, for shame, forbear this outrage! stop
Tybalt! Mercutio! The Prince expressly hath
Forbidden bandying5
 in Verona streets! this bandying2
, fighting
Hold, Tybalt! Good Mercutio!
[draws and tries to disarm them]
[Tybalt stabs Mercutio]
[A CAPULET Away, Tybalt!]+
3.1.92
MERCUTIO I am hurt. 3.1.93
A plague o' both [your]+
 houses! I am sped. death to both your families, done
[Tybalt & Capulets exit]
Is he gone and hath nothing? without a scratch
BENVOLIO What, art thou hurt? 3.1.96
MERCUTIO 3.1.97
Ay, ay, a scratch, a scratch. Marry, 'tis enough.
Where is my page?—Go, villein, fetch a surgeon! [Page exits] servant
ROMEO 3.1.99
Courage, man, the hurt cannot be much.
MERCUTIO 3.1.100
No, 'tis not so deep as a well, nor so wide as a
church door, but 'tis enough, 'twill serve. Ask for me
tomorrow, and you shall find me a grave man. I am
peppered, I warrant, for this world. A plague o' both finished, swear
your houses! Zounds, a dog, a rat, a mouse, a cat, to damn
scratch a man to death! A braggart, a rogue, a villain,
that fights by the book of arithmetic! Why the devil
came you between us? I was hurt under your arm!
ROMEO 3.1.109
I thought all for the best.
MERCUTIO 3.1.110
Help me into some house, Benvolio,
Or I shall faint. A plague o' both your houses!
They have made worms' meat of me. I have it, I've had it
And soundly too. Your houses! thoroughly
[All exit but Romeo]
ROMEO 3.1.114
This gentleman, the Prince's near ally, close relative
My very friend, hath got his mortal hurt2
fatal, wound1
In my behalf. My reputation stained
With Tybalt's slander. Tybalt, that an hour for
Hath been my cousin! O sweet Juliet,
Thy beauty hath made me effeminate weak
And in my temper softened valor's steel!
BENVOLIO [re-enters] 3.1.121
O Romeo, Romeo, brave Mercutio's5
 dead!
That gallant spirit hath aspired the clouds, risen to heaven
Which too untimely here did scorn the earth. soon, leave 
ROMEO 3.1.124
This day's black fate on more days doth depend: will have consequences
This but begins the woe others2
 must end. what other days1
[TYBALT re-enters]
BENVOLIO
Here comes the furious Tybalt back again! 3.1.126
ROMEO 3.1.127
Alive1
, in triumph! And Mercutio slain! killed
Away to heav'n, respective lenity, respectful mercy
And fire-eyed1
 fury be my conduct now!— fire and2
, guide
Now, Tybalt, take the "villain" back again that insult 3.1.130
That late thou gave'st me, for Mercutio's soul lately
Is but a little way above our heads,
Staying for thine to keep him company! waiting for your soul
Either thou, or I, or both, must go with him! go with him to heaven
TYBALT 3.1.135
Thou, wretched boy, that didst consort him here, kept company with him here
Shalt with him hence! shall be with him from now on
ROMEO This shall determine that! 3.1.137
[They fight. Romeo kills Tybalt]
BENVOLIO 3.1.138
Romeo, away, be gone!
The citizens are up, and Tybalt slain. people are coming, killed
Stand not amazed! The Prince will doom thee death dazed, sentence
If thou art taken! Hence, be gone, away! go away
ROMEO 3.1.142
O, I am Fortune's fool! fate's plaything
BENVOLIO Why dost thou stay? 3.1.143
[Romeo exits]
CITIZEN [enter] 3.1.144
Which way ran he that killed Mercutio?
Tybalt, that murderer, which way ran he?
BENVOLIO 3.1.146
There lies that Tybalt.
CITIZEN Up, sir, go with me. 3.1.147
I charge thee in the Prince's name, obey!
[PRINCE & Attendants, LORD & LADY MONTAGUE, LORD & LADY CAPULET,
and Others enter]
PRINCE 3.1.149
Where are the vile beginners of this fray? fight
BENVOLIO 3.1.150
O noble Prince, I can discover all explain
The unlucky manage of this fatal brawl. details
There lies the man, slain by young Romeo,
That slew thy kinsman, brave Mercutio.
LADY CAPULET 3.1.154
Tybalt, my cousin! O my brother's child! relative
O Prince! O cousin! Husband! O, the blood is spilt
Of my dear kinsman! Prince, as thou art true, fair
For blood of ours, shed blood of Montague! take
O cousin, cousin!
PRINCE 3.1.159
Benvolio, who began this bloody fray?
BENVOLIO 3.1.160
Tybalt, here slain, whom Romeo's hand did slay.
Romeo, that spoke him fair, bade+
 him bethink politely to him, bid2
, reminded him
How nice the quarrel was, and urged withal trivial,
Your high displeasure. All this utterèd reminded him you'd be angry
With gentle breath, calm look, knees humbly bowed, on bent knee
Could not take truce with the unruly spleen calm down, temper 3.1.165
Of Tybalt, deaf to peace, but that he tilts thrusts
With piercing steel at bold Mercutio's breast,
Who, all as hot, turns deadly point to point, angry, draws his sword
And, with a martial scorn, with one hand beats military skill,
Cold death aside and with the other sends defends against death 3.1.170
It back to Tybalt, whose dexterity skill
Retorts it. Romeo he cries aloud, avoids
"Hold, friends! Friends, part!" and swifter than his tongue
His agile1
 arm beats down their fatal points, knocks aside, swords 3.1.175
And 'twixt them rushes, underneath whose arm rushes between them
An envious thrust from Tybalt hit the life vicious
Of stout Mercutio, and then Tybalt fled, brave
But by and by comes back to Romeo, soon
Who had but newly entertained revenge, only then considered 3.1.180
And to't they go like lightning, for, ere I before
Could draw to part them, was stout Tybalt slain, bold
And as he fell did Romeo turn and fly. flee
This is the truth, or let Benvolio die. I swear on my life
LADY CAPULET 3.1.185
He is a kinsman to the Montague.
Affection makes him false; he speaks not true! lie
Some twenty of them fought in this black strife, feud
And all those twenty could but kill one life. only
I beg for justice, which thou, Prince, must give.
Romeo slew Tybalt. Romeo must not live!
PRINCE 3.1.191
Romeo slew him; he slew Mercutio.
Who now the price of his dear blood doth owe? Mercutio's
MONTAGUE4
3.1.193
Not Romeo, Prince, he was Mercutio's friend.
His fault concludes but what the law should end: crime, only
The life of Tybalt.
PRINCE And for that offence 3.1.196
Immediately we do exile him hence. banish him from Verona
I have an interest in your hate's1
 proceeding: hearts'2
My blood for your rude brawls doth lie a-bleeding. relative, barbaric
But I'll amerce you with so strong a fine punish, heavy 3.1.200
That you shall all repent the loss of mine! regret
I
1
 will be deaf to pleading and excuses.
Nor tears nor prayers shall purchase out abuses. buy your way out of this
Therefore use none! Let Romeo hence in haste, go away
Else, when he's found, that hour is his last! 3.1.205
Bear hence this body and attend our will. carry away, come to hear more
Mercy but murders, pardoning those that kill. just causes more
[All exit]
ACT 3, SCENE 2
[Capulet house. JULIET]
JULIET 3.2.1
Gallop apace, you fiery-footed steeds, fast, horse
Towards Phoebus' lodging. Such a wagoner the sun god's home, driver
As Phaeton would whip you to the west the sun god's sun
And bring in cloudy night immediately.
Spread thy close curtain, love-performing night, 3.2.5
That runaways' eyes may wink, and Romeo those horses eyes may close
Leap to these arms, untalked-of and unseen. without being talked about
Lovers can see to do their amorous rites love making
By4
 their own beauties. Or, if love be blind, And by2
: by the light of
It best agrees with night. Come, civil night, love likes night best, solemn
Thou sober-suited matron all in black, somberly dressed 3.2.11
And learn me how to lose a winning match teach, win by losing this game
Played for a pair of stainless maidenhoods. our virginities
Hood my unmanned blood, bating in my cheeks, cover, untamed, fluttering
With thy black mantle till strange love grow bold, cloak, my shy love 3.2.15
Think true love acted simple modesty. acted in foolish modesty
Come, night. Come, Romeo. Come thou day in night.
For thou wilt lie upon the wings of night
Whiter than new snow upon2
 a raven's back. on+
 3.2.20
Come gentle night. Come loving black-browed night. black faced
Give me my Romeo, and when he+
 shall die, I
2
Take him and cut him out in little stars,
And he will make the face of heav'n so fine 3.2.25
That all the world will be in love with night
And pay no worship to the garish sun. gaudy
O, I have bought the mansion of a love called love
But not possessed it, and though I am sold, occupied
Not yet enjoyed. So tedious is this day enjoyed by my new owner, long
As is the night before some festival 3.2.31
To an impatient child that hath new robes clothes
And may not wear them. O, here comes my Nurse,
And she brings news, and every tongue that speaks
But Romeo's name speaks heavenly eloquence. just
[NURSE enters with rope-ladder]
Now, Nurse, what news? What hast thou there? The cords 3.2.37
That Romeo bid thee fetch?
NURSE Ay, ay, the cords. 3.2.40
JULIET 3.2.41
Ay me, what news? Why dost thou wring thy hands?
NURSE 3.2.42
Ah, weraday! He's dead, he's dead, he's dead! woe the day
We are undone, lady, we are undone! ruined
Alack the day! He's gone, he's killed, he's dead!
JULIET 3.2.45
Can heaven be so envious? vicious
NURSE Romeo can, 3.2.46
Though heaven cannot. O Romeo, Romeo!
Who ever would have thought it? Romeo!
JULIET 3.2.49
What devil art thou that dost torment me thus?
This torture should be roared in dismal hell!
Hath Romeo slain himself? Say thou but "ay" just
And that bare vowel "I" shall poison more be more poisonous to myself
Than the death-darting eye of cockatrice! deadly eye, a mythical serpent
I am not I if there be such an "ay", I'll no longer be myself 3.2.54
Or those eyes shut, that make thee answer "ay". or if Romeo's eyes are shut
If he be slain, say "ay", or if not, "no"!
Brief sounds determine of my weal or woe! those brief words, happiness
NURSE 3.2.58
I saw the wound, I saw it with mine eyes
—God save the mark—here on his manly breast. God save me
A piteous corse, a bloody piteous corse, pitiful corpse
Pale, pale as ashes, all bedaubed in blood, covered
All in gore-blood. I swoonèd at the sight. gory, fainted 
JULIET 3.2.63
O, break, my heart! Poor bankrupt, break at once! ruined heart
To prison, eyes; ne'er look on liberty!
Vile earth to earth resign! End motion here! my earthly body, rest, life
And thou and Romeo press one heavy bier! my body, lay on, funeral bed
NURSE 3.2.67
O Tybalt, Tybalt, the best friend I had!
O courteous Tybalt, honest gentleman!
That ever I should live to see thee dead!
JULIET 3.2.70
What storm is this that blows so contrary? much grief
Is Romeo slaughtered and is Tybalt dead?
My dearest cousin, and my dearer lord? husband
Then, dreadful trumpet, sound the general doom! end of the world
For who is living, if those two are gone?
NURSE 3.2.75
Tybalt is gone, and Romeo banishèd. banished from Verona
Romeo that killed him, he is banishèd.
JULIET 3.2.77
O God! Did Romeo's hand shed Tybalt's blood?
NURSE1
JULIET2
 3.2.78
It did, it did, alas the day, it did!
JULIET1
3.2.79
O serpent heart, hid with a flowering face! disguised, lovely
Did ever dragon keep so fair a cave? beautiful
Beautiful tyrant, fiend angelical!
Dove-feathered raven! Wolvish-ravening lamb! wolf-like lamb
Despisèd substance of divinest show! reality of heavenly appearance
Just opposite to what thou justly seem'st.
A damnèd4
 saint, an honorable villain! dim2
 3.2.85
O nature, what hadst thou to do in hell what were you doing
When thou didst bower the spirit of a fiend enclose, devil
In mortal paradise of such sweet flesh? such lovely human form
Was ever book containing such vile matter was there ever a
So fairly bound? O, that deceit should dwell with such a beautiful cover
In such a gorgeous palace!
NURSE There's no trust, 3.2.92
No faith, no honesty in men. All perjured, liars
All forsworn, all naught, all dissemblers. deceitful, worthless, false
Ah, where's my man? Give me some aqua vitae. servant, brandy
These griefs, these woes, these sorrows make me old.
Shame come to Romeo! shame on Romeo
JULIET Blistered be thy tongue 3.2.99
For such a wish! He was not born to shame!
Upon his brow2
 shame is ashamed to sit, face1
For 'tis a throne where honor may be crowned
Sole monarch of the universal earth! 3.2.103
O, what a beast was I to chide at him! criticize
NURSE 3.2.105
Will you speak well of him that killed your cousin?
JULIET 3.2.106
Shall I speak ill of him that is my husband?
Ah, poor my lord, what tongue shall smooth thy name husband
When I, thy three-hours wife, have mangled it?
But, wherefore, villain, didst thou kill my cousin? why 3.2.110
That villain cousin would have killed my husband.
Back, foolish tears, back to your native spring! back into my eyes
Your tributary drops belong to woe, stream of
Which you, mistaking, offer up to joy. 
My husband lives, that Tybalt would have slain, 3.2.115
And Tybalt's dead, that would have slain my husband.
All this is comfort. Wherefore weep I then? why
Some word there was, worser than Tybalt's death,
That murdered me. I would forget it fain, gladly 3.2.120
But O, it presses to my memory
Like damnèd guilty deeds to sinners' minds.
"Tybalt is dead, and Romeo...banishèd."
That "banishèd," that one word "banishèd"
Hath slain ten thousand Tybalts. Tybalt's death 3.2.125
Was woe enough if it had ended there.
Or if sour woe delights in fellowship wants company
And needly will be ranked with other griefs, must be accompanied
Why followed not, when she said "Tybalt's dead,"
Thy father, or thy mother, nay, or both, 3.2.130
Which modern lamentation might have moved? a normal amount of sadness
But with a rearward following Tybalt's death, those words
"Romeo is banishèd." To speak that word
Is father, mother, Tybalt, Romeo, Juliet, is like saying
All slain, all dead! "Romeo is banishèd!" 3.2.135
There is no end, no limit, measure, bound, measurement, boundary
In that word's death. No words can that woe sound. in the death that brings,
Where is2
 my father and my mother, Nurse? are1
, express that woe
NURSE 3.2.139
Weeping and wailing over Tybalt's corse. corpse
Will you go to them? I will bring you thither. there
JULIET 3.2.141
Wash they his wounds with tears? Mine shall be spent used up
When theirs are dry, for Romeo's banishment.
Take up those cords. Poor ropes, you are beguiled, pick up that rope-ladder, cheated
Both you and I, for Romeo is exiled.
He made you for a highway to my bed, 3.2.147
But I, a maid, die maiden-widowed. virgin, will die a virgin widow
Come, cords. Come, Nurse, I'll to my wedding-bed,
And Death, not Romeo, take my maidenhead! will take my virginity
NURSE 3.2.151
Hie to your chamber. I'll find Romeo hurry, bedroom
To comfort you. I wot well where he is. know
Hark ye, your Romeo will be here at night. listen
I'll to him. He is hid at Lawrence' cell. go to
JULIET 3.2.155
O, find him! Give this ring to my true knight, [hands her a ring]
And bid him come to take his last farewell.
[They exit]
ACT 3, SCENE 3
[Church, that night. FRIAR, ROMEO]
FRIAR 3.3.1
Romeo, come forth. Come forth, thou fearful man. come in
Affliction is enamored of thy parts, suffering is in love with you
And thou art wedded to calamity. married to misfortune
ROMEO 3.3.4
Father, what news? What is the Prince's doom? punishment
What sorrow craves acquaintance at my hand wishes to meet me
That I yet know not? 
FRIAR Too familiar 3.3.7
Is my dear son with such sour company.
I bring thee tidings of the Prince's doom. news, sentence
ROMEO 3.3.10
What less than doomsday is the Prince's doom? short of
FRIAR 3.3.11
A gentler judgment vanished from his lips: passed
Not body's death, but body's banishment. your
ROMEO 3.3.13
Ha! Banishment? Be merciful, say "death"! what (not laughing)
For exile hath more terror in his look,
Much more than death! Do not say "banishment"!
FRIAR 3.3.16
Hence from Verona art thou banishèd. away
Be patient, for the world is broad and wide.
ROMEO 3.3.18
There is no world without Verona walls, outside
But purgatory, torture, hell itself!
Hence "banishèd" is "banish'd from the world," therefore, means
And world's exile is death! Then "banishèd" exile from the world means
Is death mis-termed. Calling death "banishèd," misnamed
Thou cutt'st my head off with a golden axe
And smile'st upon the stroke that murders me.
FRIAR 3.3.25
O deadly sin! O rude unthankfulness!
Thy fault our law calls death, but the kind Prince, crime is punishable by
Taking thy part, hath rushed aside the law taking your side, brushed
And turned that black word "death" to "banishment."
This is dear mercy, and thou see'st it not.
ROMEO 3.3.31
'Tis torture, and not mercy! Heav'n is here
Where Juliet lives, and every cat and dog
And little mouse, every unworthy thing,
Live here in heaven and may look on her,
But Romeo may not. More validity, value 3.3.35
More honorable state, more courtship lives status, courtliness
In carrion-flies than Romeo. They my seize common flies, land
On the white wonder of dear Juliet's hand
And steal immortal blessing2
 from her lips, heavenly, kisses1
Who even in pure and vestal modesty virginal 3.3.40
Still blush, as thinking their own kisses sin. always, kisses to each other a
But Romeo may not; he is banishèd.
Flies may do this, but I from this must fly. flee
They are free men, but I am banishèd.
And say'st thou yet that exile is not death? 3.3.45
Hadst thou no poison mixed, no sharp-ground knife,
No sudden mean of death, though ne'er so mean, no matter how dishonorable
But "banishèd" to kill me? "Banishèd"? other than
O Friar, the damnèd use that word in hell! damned souls 3.3.50
Howling attends it! How hast thou the heart, accompanies
Being a divine, a ghostly confessor, priest, spiritual
A sin-absolver, and my friend professed, one who calls himself my friend
To mangle me with that word "banishèd"? tear me apart
FRIAR 3.3.55
Thou1
 fond madman, hear me but speak a word1
. then2
, foolish, a little speak2
ROMEO 3.3.56
O, thou wilt speak again of banishment.
FRIAR 3.3.57
I'll give thee armor to keep off that word: protection
Adversity's sweet milk, philosophy,
To comfort thee, though thou art banishèd.
ROMEO 3.3.60
Yet "banishèd"? Hang up philosophy! damn
Unless philosophy can make a Juliet,
Displant a town, reverse a Prince's doom, move, sentence
It helps not, it prevails not! Talk no more! it has no power
FRIAR 3.3.64
O, then I see that madmen1
 have no ears.
ROMEO 3.3.65
How should they when that wise men have no eyes? why
FRIAR 3.3.66
Let me dispute with thee of thy estate. reason with you about your situation
ROMEO 3.3.67
Thou canst not speak of that2
 thou dost not feel! what1
Wert thou as young as I, Juliet thy love, and Juliet were your love
An hour but married, Tybalt murderèd,
Doting like me, and like me banishèd, in love like me
Then mightst thou speak, then mightst thou tear thy hair tear out
And fall upon the ground, as I do now,
Taking the measure of an unmade grave. measurement of my
[NURSE knocks at door]
FRIAR 3.3.75
Arise. One knocks. Good Romeo, hide thyself.
ROMEO 3.3.76
Not I, unless the breath of heartsick groans, my brokenhearted groans
Mist-like, enfold me from the search of eyes. hides me in its mist
[Knocking]
FRIAR 3.3.78
Hark, how they knock!—Who's there?—Romeo, arise,
Thou wilt be taken!
[Knocking] —Stay awhile!—Stand up, wait a minute
Run to my study!
[Knocking] —By and by!—God's will, just a minute
What simpleness is this! foolishness
[Knocking] —I come, I come!
Who knocks so hard? Whence come you? What's your will? from where,
NURSE [outside] what do you want
Let me come in, and you shall know my errand. 3.3.85
I come from Lady Juliet.
FRIAR [opens door] Welcome then! 3.3.87
NURSE [enters] 3.3.88
O Holy Friar, O, tell me, Holy Friar,
Where is1
 my lady's lord? Where's Romeo? where's2
, husband
FRIAR 3.3.90
There on the ground, with his own tears made drunk.
NURSE 3.3.92
O, he is even in my mistress' case, in the same condition as Juliet
Just in her case! O woeful sympathy! same condition
Piteous predicament! Even so lies she, pitiful, she lies the same way
Blubbering and weeping, weeping and blubbering.
[to Romeo] Stand up, stand up! Stand, and you be a man! if
For Juliet's sake, for her sake, rise and stand!
Why should you fall into so deep an O? groaning
ROMEO 3.3.99
Nurse!
NURSE Ah sir, ah sir! Death's the end of all. all of us 3.3.100
ROMEO 3.3.101
Spake'st thou of Juliet? How is it with her? 
Doth she not think me an old murderer,
Now I have stained the childhood of our joy ruined the beginning
With blood removed but little from her own? of her close relative
Where is she? And how doth she? And what says
My concealed lady to our cancelled love? secret bride about
NURSE 3.3.107
O, she says nothing, sir, but weeps and weeps,
And now falls on her bed, and then starts up,
And "Tybalt" calls, and then on Romeo cries, calls out "Tybalt", about
And then down falls again.
ROMEO As if that name, my name 3.3.111
Shot from the deadly level of a gun, aim
Did murder1
 her, as that name's cursèd hand
Murdered her kinsman! O, tell me, Friar, tell me,
In what vile part of this anatomy my body
Doth my name lodge2
? Tell me, that I may sack lie1
: live, pillage
The hateful mansion! [tries to stab himself] hated place
FRIAR Hold thy desperate hand! 3.3.118
Art thou a man? Thy form cries out thou art! you look like you are
Thy tears are womanish, thy wild acts denote1
seem like
The unreasonable fury of a beast!
Unseemly woman in a seeming man, improper, what looks like a man
And ill-beseeming beast in seeming both! unnatural, for looking like both
Thou hast amazed me! By my holy order,
I thought thy disposition better tempered. character, balanced 3.3.125
Hast thou slain Tybalt! Wilt thou slay thyself? so you've killed Tybalt
And slay thy lady that in thy life lives1
, wife who is one with your life
By doing damnèd hate upon thyself? committing suicide
Why rail'st thou on thy birth, the heav'n and earth, complain, soul, body
Since birth and heav'n and earth, all three do meet soul, body 3.3.130
In thee at once, which thou at once wouldst lose?
Fie, fie, thou shame'st thy shape, thy love, thy wit, disgrace, body, mind
Which, like a usurer, abound'st in all, moneylender, surrounded, possessions
And usest none in that true use indeed for their proper purpose
Which should bedeck thy shape, thy love, thy wit. improve, body, mind
Thy noble shape is but a form of wax, body, figure 3.3.136
Digressing from the valor of a man; lacking the courage
Thy dear love sworn but hollow perjury, you've sworn is just an empty lie
Killing that love which thou hast vowed to cherish;
Thy wit, that ornament to shape and love, mind, body 3.3.140
Misshapen in the conduct of them both, mistaken in the guidance
Like powder in a skilless soldier's flask, gunpowder, unskilled, powder-horn
Is set afire by thine own ignorance,
And thou dismembered with thine own defense! blown apart, weapon
What, rouse thee, man! Thy Juliet is alive, cheer up 3.3.145
For whose dear sake thou wert1
 but lately dead. wast2
: just now wished to be dead
There art thou happy! Tybalt would kill thee, you are fortunate
But thou slew'st Tybalt. There are thou happy! you are fortunate
The law that threatened death becomes thy friend
And turns it to exile. There art thou happy! you are fortunate 3.3.150
A pack of blessings lights up upon thy back; many blessings are on you
Happiness courts thee in her best array; good fortune, clothes
But, like a misbehaved1
 and sullen wench, sulking girl
Thou pouts+
 upon1
 thy fortune and thy love. frownst1
Take heed, take heed, for such die miserable. be careful, such people
Go, get thee to thy love, as was decreed, you planned 3.3.156
Ascend her chamber. Hence and comfort her. climb into her bedroom, go on
But look thou stay not till the watch be set, be sure, night guards go on duty
For then thou canst not pass to Mantua, leave
Where thou shalt live till we can find a time find the right time 3.3.160
To blaze your marriage, reconcile your friends, announce, families
Beg pardon of the Prince, and call thee back
With twenty hundred thousand times more joy
Than thou went'st forth in lamentation. sorrow 3.3.164
[to Nurse] Go before, Nurse. Commend me to thy lady, ahead, my regards
And bid her hasten all the house to bed, urge everyone to bed early
Which heavy sorrow makes them apt unto. ready to do
Romeo is coming.
NURSE 3.3.169
O Lord, I could have stayed here all the night
To hear good counsel. O, what learning is! advice, education
[to Romeo] My lord, I'll tell my lady you will come!
ROMEO 3.3.172
Do so, and bid my sweet prepare to chide. sweetheart, scold me
NURSE 3.3.173
Here, sir, a ring she bid me give you, sir. [hands him the ring]
Hie you, make haste, for it grows very late! [exits] hurry
ROMEO 3.3.175
How well my comfort is revived by this! spirit
FRIAR 3.3.176
Go hence, good night, and here stands all your state: all depends on this
Either be gone before the watch be set night guards go on duty
Or by the break of day disguised3
 from hence. by dawn leave in disguise
Sojourn in Mantua. I'll find out your man, stay, find your servant
And he shall signify from time to time bring messages
Every good hap to you that chances here. all good news, happens
Give me thy hand. 'Tis late. Farewell. Good night.
ROMEO 3.3.184
But that a joy past joy calls out on me, if it weren't for a joy beyond joys
It were a grief, so brief to part with thee. that calls me away, it would be
Farewell. sad to leave you in such hurry
[They exit]
ACT 3, SCENE 4
[Capulet house. LORD & LADY CAPULET, PARIS]
CAPULET 3.4.1
Things have fallen out, sir, so unluckily
That we have had no time to move our daughter. persuade
Look you, she loved her kinsman Tybalt dearly,
And so did I. Well, we were born to die.
'Tis very late. She'll not come down tonight. come down from her room
I promise you, but for your company, if not
I would have been a-bed an hour ago. in bed
PARIS 3.4.8
These times of woe afford no time1
 to woo. allow, times2
Madam, good night. Commend me to your daughter. give my regards
LADY CAPULET 3.4.11
I will, and know her mind early tomorrow. I'll know what she thinks
Tonight she's mewed up to her heaviness. closed off in her sorrow
CAPULET 3.4.13
Sir Paris, I will make a desperate tender bold offer
Of my child's love. I think she will be1
 ruled
In all respects by me. Nay, more, I doubt it not.
Wife, go you to her ere you go to bed, before
Acquaint her here of my son Paris' love, tell, son-in-law
And bid her—mark you me?—on Wednesday next— are you listening
But soft, what day is this? wait
PARIS Monday, my lord. 3.4.21
CAPULET 3.4.22
Monday! Ha, ha. Well, Wednesday is too soon. ah (not laughing)
O' Thursday let it be. [to her] O' Thursday, tell her,
She shall be married to this noble earl!
[to him] Will you be ready? Do you like this haste? approve, speed
We'll keep2
 no great ado, a friend or two, make1
: not have a big affair
For hark you, Tybalt being slain so late, listen, recently
It may be thought we held him carelessly, thought little of him
Being our kinsman, if we revel much. celebrate
Therefore we'll have some half a dozen friends,
And there an end. But what say you to Thursday? that's all
PARIS 3.4.32
My lord, I would that Thursday were tomorrow! wish
CAPULET 3.4.33
Well get you gone. O' Thursday be it, then!
[to her] Go you to Juliet ere you go to bed, before
Prepare her, wife, against this wedding day. for
[to him] Farewell, my lord.
[to Servant] Light to my chamber, ho! bring lights, room
[to him] Afore me, it is so very late that we oh my
May call it early by and by. Good night. soon
[They exit]
ACT 3, SCENE 5
[Juliet's bedroom, dawn. ROMEO & JULIET]
JULIET 3.5.1
Wilt thou be gone? It is not yet near day.
It was the nightingale, and not the lark,
That pierced the fearful hollow of thine ear. you heard
Nightly she sings on yon1
 pomegranate tree. yond2
: that
Believe me, love, it was the nightingale.
ROMEO 3.5.6
It was the lark, the herald of the morn,
No nightingale. Look, love, what envious streaks streaks of light
Do lace the severing clouds in yonder east. pierce the clouds
Night's candles are burnt out, and jocund day stars, jolly
Stands tiptoe on the misty mountain-tops.
I must be gone and live, or stay and die.
JULIET 3.5.12
Yon1
 light is not daylight, I know it, I. yond2
: that
It is some meteor that the sun exhaled+
,
To be to thee this night a torchbearer
And light thee on thy way to Mantua.
Therefore stay yet. Thou need'st not to be gone.
ROMEO 3.5.17
Let me be ta'en; let me be put to death. captured
I am content, so thou wilt have it so. if
I'll say yon grey is not the morning's eye; that grey light
'Tis but the pale reflex of Cynthia's brow. reflection of the moon's face
Nor that is not the lark, whose notes do beat song rises to
The vaulty heav'n so high above our heads. 3.5.22
I have more care to stay than will to go. desire, willpower
Come death, and welcome; Juliet wills it so! wishes
How is't, my soul? Let's talk. It is not day. how are you, my love 
JULIET [realizing it is late] 3.5.26
It is, it is! Hie hence, be gone, away! hurry away
It is the lark that sings so out of tune,
Straining harsh discords and unpleasing sharps.
Some say the lark makes sweet division. music
This doth not so, for she divideth us! separates 3.5.30
Some say the lark and loathèd toad changed+
 eyes. ugly, change2
: exchanged
O, now I would they had changed voices too, wish, exchanged
Since arm from arm that voice doth us affray, from each other's arms, tear us
Hunting thee hence with hunt's-up to the day. chasing, away, morning call
O, now be gone! More light and light it grows.
ROMEO 3.5.36
More light and light, more dark and dark our woes! the lighter it grows
NURSE [enters] the darker our woes
Madam! 3.5.37
JULIET 3.5.38
Nurse?
NURSE 3.5.39
Your lady mother is coming to your chamber! room
The day is broke. Be wary. Look about! [exits] it's daybreak, careful, watch out
JULIET 3.5.41
Then, window, let day in, and let life out!
ROMEO 3.5.42
Farewell, farewell! One kiss, and I'll descend. [goes down]
JULIET 3.5.43
Art thou gone so? Love, lord, ay, husband, friend!
I must hear from thee every day in the hour, and every hour
For in a minute there are many days.
O, by this count I shall be much in years very old
Ere I again behold my Romeo! before, see
ROMEO 3.5.48
Farewell!
I will omit no opportunity miss no chance
That may convey my greetings, love, to thee. to send
JULIET 3.5.51
O think'st thou we shall ever meet again?
ROMEO 3.5.52
I doubt it not, and all these woes shall serve of these woes we'll
For sweet discourses in our time5
 to come. times2
: talk and laugh years from now
JULIET1
3.5.54
O God, I have an ill-divining soul! bad feeling
Methinks I see thee, now thou art below1
, I think, so low2
As one dead in the bottom of a tomb.
Either my2
 eyesight fails, or thou look'st pale. mine1
ROMEO 3.5.58
And trust me, love, in my eye so do you.
Dry sorrow drinks our blood. Adieu, adieu! [exits] thirsty, drains, farewell
JULIET 3.5.60
O Fortune, Fortune! All men call thee fickle. quick to change your mind
If thou art fickle, what dost thou with him what do you want with him
That is renowned for faith? Be fickle, Fortune, well known for faithfulness
For then I hope thou wilt not keep him long,
But send him back!
LADY CAPULET [off-stage] Ho, daughter, are you up? 3.5.65
JULIET 3.5.66
Who is't that calls? It is my lady mother.
Is she not down so late, or up so early? still awake
What unaccustomed cause procures her hither? unusual event brings, here 
LADY CAPULET [enters] 3.5.69
Why, how now, Juliet? how are you
JULIET Madam, I am not well. 3.5.70
LADY CAPULET 3.5.71
Evermore weeping for your cousin's death? still
What, wilt thou wash him from his grave with tears?
And if thou couldst, thou couldst not make him live.
Therefore, have done. Some grief shows much of love, stop crying, a little
But much of grief shows still some want of wit. foolishness
JULIET 3.5.77
Yet let me weep for such a feeling loss. deep
LADY CAPULET 3.5.78
So shall you feel the loss, but not the friend but Tybalt whom you
Which you weep for. weep for cannot feel
JULIET Feeling so the loss, the loss so much 3.5.80
I cannot choose but ever weep the friend. for the
LADY CAPULET 3.5.82
Well, girl, thou weep'st not so much for his death,
As that the villain lives which slaughtered him. as because that villain
JULIET 3.5.84
What villain madam?
LADY CAPULET That same villain Romeo. 3.5.85
JULIET 3.5.86
[aside] Villain and he be many miles asunder. he's miles from being a villain
[to her] God pardon him4
. I do, with all my heart.
And yet no man like he doth grieve my heart. anger me / my heart miss
LADY CAPULET 3.5.89
That is because the traitor murd'rer lives.
JULIET 3.5.90
Ay, madam, from the reach of these my hands. beyond
Would none but I might venge my cousin's death! I wish I alone, avenge
LADY CAPULET 3.5.92
We will have vengeance for it, fear thou not!
Then weep no more. I'll send to one in Mantua, send a message to someone
Where that same banish'd runagate doth live, fugitive
Shall give him such an unaccustomed dram who will, strange drink (poison)
That he shall soon keep Tybalt company.
And then, I hope, thou wilt be satisfied.
JULIET 3.5.98
Indeed, I never shall be satisfied
With Romeo till I behold him...dead...
Is my poor heart so for a kinsman vexed. cousin dead / husband exiled
Madam, if you could find out but a man find such a man
To bear a poison, I would temper it, carry the, mix / dilute
That Romeo should, upon receipt thereof, receiving it
Soon sleep in quiet. O, how my heart abhors die / sleep, hates
To hear him named and cannot come to him 3.5.105
To wreak the love I bore my cousin avenge / give, held for
Upon his body that hath slaughtered him!
LADY CAPULET 3.5.108
Find thou the means, and I'll find such a man. poison
But now I'll tell thee joyful tidings, girl! news
JULIET 3.5.110
And joy comes well in such a needy time.
What are they, I beseech your ladyship?
LADY CAPULET 3.5.112
Well, well, thou hast a careful father, child, caring
One who, to put thee from thy heaviness, end your sorrow
Hath sorted out a sudden day of joy has arranged
That thou expects not, nor I looked not for. expected
JULIET 3.5.116
Madam, in happy time! What day is that? good
LADY CAPULET 3.5.117
Marry, my child, early next Thursday morn, well, morning
The gallant, young and noble gentleman,
The County Paris, at Saint Peter's Church, Count
Shall happily make thee there a joyful bride!
JULIET 3.5.121
Now, by Saint Peter's Church and Peter too,
He shall not make me there a joyful bride!
I wonder at this haste, that I must wed am shocked
Ere he that should be husband comes to woo! before
I pray you, tell my lord and father, madam,
I will not marry yet! And, when I do, I swear,
It shall be Romeo, whom you know I hate,
Rather than Paris. These are news indeed!
LADY CAPULET 3.5.129
Here comes your father. Tell him so yourself,
And see how he will take it at your hands. take it from you
[CAPULET & NURSE enter]
CAPULET 3.5.131
When the sun sets, the air doth drizzle dew,
But for the sunset of my brother's son death
It rains downright.
How now, a conduit, girl? What, still in tears? what's this, fountain
Evermore showering? In one little body still 3.5.135
Thou counterfeits a bark, a sea, a wind, imitate, boat
For still thy eyes, which I may call the sea,
Do ebb and flow with tears. The bark thy body is, body
Sailing in this salt flood. The winds, thy sighs,
Who, raging with thy tears and they with them, 3.5.140
Without a sudden calm, will overset unless there's, capsize
Thy tempest-tossèd body.—How now, wife! storm-tossed
Have you delivered to her our decree? told her our decision
LADY CAPULET 3.5.144
Ay, sir, but she will none; she gives you thanks. she'll have none of it
I would the fool were married to her grave! wish
CAPULET 3.5.146
Soft, take me with you, take me with you, wife. wait, explain this to me
How! Will she none? Doth she not give us thanks? have none of it
Is she not proud? Doth she not count her blest, happy, consider herself blessed
Unworthy as she is, that we have wrought arranged
So worthy a gentleman to be her bridegroom5
? bride2
: make her a bride
JULIET 3.5.151
Not proud you have, but thankful that you have. I'm not happy that
Proud can I never be of what I hate,
But thankful even for hate that is meant love. but I'm, you meant for me to
CAPULET 3.5.154
How, how2
, how, how2
? Chopped logic? What is this? now5
, now5
, quibbling
"Proud" and "I thank you" and "I thank you not"
And yet "not proud"? Mistress minion you, spoiled hussy
Thank me no thankings, nor proud me no prouds,
But fettle your fine joints 'gainst Thursday next prepare your fine self for
To go with Paris to Saint Peter's Church,
Or I will drag thee on a hurdle thither! cart, there 3.5.160
Out, you green-sickness carrion! Out, you baggage! rotten thing, good-for-nothing
You tallow-face! coward 
LADY CAPULET Fie, fie. What, are you mad? shame on you 3.5.163
JULIET 3.5.164
Good father, I beseech you on my knees,
Hear me with patience but to speak a word.
CAPULET 3.5.166
Hang thee, young baggage! Disobedient wretch! damn, good-for-nothing
I tell thee what: get thee to church o' Thursday,
Or never after look me in the face! look at me
Speak not, reply not, do not answer me! shut up, don't talk back
My fingers itch!—Wife, we scarce thought us blest I'll hit you, thought ourselves blest
That God had lent us but this only child, given 3.5.172
But now I see this one is one too much,
And that we have a curse in having her.
Out on her, hilding! damn her, worthless creature
NURSE God in heav'n bless her! 3.5.176
You are to blame, my lord, to rate her so! scold
CAPULET 3.5.178
And why, my Lady Wisdom? Hold your tongue,
Good Prudence! Smatter with your gossips, go! Miss Know-It-All, chatter,
NURSE gossipy old ladies 3.5.180
I speak no treason— nothing disloyal
CAPULET O, God 'i' good e'en! get on with you 3.5.181
NURSE 3.5.182
May not one speak?
CAPULET Peace, you mumbling fool! 3.5.183
Utter your gravity o'er a gossip's1
 bowl, wisdom in your gossip circle
For here we need it not!
LADY CAPULET You are too hot! upset 3.5.186
CAPULET 3.5.187
God's bread! It makes me mad! damn it
Day, night, hour, tide, time, work, play, season, at work
Alone, in company, still my care hath been with, all I think about
To have her matched. And having now provided is getting her married
A gentleman of noble parentage, 3.5.191
Of fair demesnes, youthful, and nobly liened2
, "di·máins": estates,
Stuffed, as they say, with honorable parts, well connected / trained1
, qualities
Proportioned as one's thought would wish a man; handsome, one could
And then to have a wretched puling fool, whimpering
A whining mammet, in her fortune's tender, doll, receiving good fortune
To answer "I'll not wed; I cannot love, 3.5.197
I am too young, I pray you pardon me!"
[to Juliet] But if1
 you will not wed, I'll "pardon" you: and2
 3.5.199
Graze where you will, you shall not house with me! go eat, stay in this house
Look to't. Think on't. I do not use to jest! joke
Thursday is near. Lay hand on heart. Advise. look in your, consider it
If1
 you be mine, I'll give you to my friend. and2
, if you're my daughter
If1
 you be not, hang! Beg! Starve! Die in the streets! and2
, if you're not 3.5.204
For, by my soul, I'll ne'er acknowledge thee! you as my daughter
Nor what is mine shall never do thee good! will you get anything from me
Trust to't. Bethink you. I'll not be forsworn! think on it, take back my words
[exits]
JULIET 3.5.208
Is there no pity sitting in the clouds in heaven
That sees into the bottom of my grief?— depth
O, sweet my mother, cast me not away! don't send me away
Delay this marriage for a month! A week!
Or if you do not, make the bridal bed
In that dim monument where Tybalt lies. tomb 
LADY CAPULET 3.5.214
Talk not to me, for I'll not speak a word.
Do as thou wilt, for I have done with thee. [exits] do what you will
JULIET 3.5.216
O God! O Nurse, how shall this be prevented?
My husband is on earth, my faith in heaven. alive, marriage vow sworn
How shall that faith return again to earth can I marry again
Unless that husband send it me from heaven
By leaving earth? Comfort me, counsel me! dying, advise 3.5.220
Alack, alack, that heav'n should practice stratagems set traps
Upon so soft a subject as myself! weak, person
What say'st thou? Hast thou not a word of joy?
Some comfort, Nurse.
NURSE Faith, here it is. 3.5.225
Romeo is banished, and all the world to nothing you can bet the world
That he dares ne'er come back to challenge you, claim
Or if he do, it needs must be by stealth. he'll have to do it in secret
Then, since the case so stands as now it doth, so, the way things stand
I think it best you married with the County. Count Paris 3.5.230
O, he's a lovely gentleman!
Romeo's a dish-clout to him. An eagle, madam, dishrag compared to him
Hath not so green, so quick, so fair an eye
As Paris hath. Beshrew my very heart, curse me if I'm wrong
I think you are happy in this second match, fortunate, marriage 3.5.235
For it excels your first; or if it did not, is better than
Your first is dead, or 'twere as good he were as good as dead
As living here and you no use of him. on earth, never able to see you
JULIET 3.5.239
Speakest thou from thy heart?
NURSE 3.5.240
And from my soul too, else beshrew them both. curse
JULIET 3.5.241
Amen.
NURSE 3.5.242
What?
JULIET 3.5.243
Well, thou hast comforted me marvelous much.
Go in and tell my lady I am gone, mother
Having displeased my father, to Lawrence' cell,
To make confession and to be absolved. forgiven
NURSE 3.5.247
Merry, I will; and this is wisely done. [exits]
JULIET 3.5.248
Ancient damnation! O most wicked fiend! cursed old woman
Is it more sin to wish me thus forsworn, to break my wedding vow
Or to dispraise my lord with that same tongue criticize, husband
Which she hath praised him with above compare beyond comparison
So many thousand times? Go, counselor. 3.5.252
Thou and my bosom henceforth shall be twain. you'll never hear my secrets
I'll to the Friar to know his remedy.
If all else fail, myself have power to die. [exits] kill myself
ACT 4, SCENE 1
[Church, later that day. FRIAR & PARIS]
FRIAR 4.1.1
On Thursday, sir? The time is very short. 
PARIS 4.1.2
My father Capulet will have it so, father-in-law
And I am nothing slow to slack his haste. not unwilling to slow him down
FRIAR 4.1.4
You say you do not know the lady's mind? thoughts on this
Uneven is the course. I like it not. this is too irregular
PARIS 4.1.6
Immoderately she weeps for Tybalt's death, excessively
And therefore have I little talked1
 of love, talk2
For Venus smiles not in a house of tears. the god of love
Now, sir, her father counts it dangerous considers
That she doth1
 give her sorrow so much sway, do2
, let sorrow overwhelm her
And in his wisdom hastes our marriage hurries 4.1.11
To stop the inundation of her tears, flood
Which, too much minded by herself alone, she thinks about too much when
May be put from her by society. being with others may help her forget
Now do you know the reason of this haste.
FRIAR 4.1.16
[aside] I would I knew not why it should be slowed. wish, postponed
[JULIET enters]
Look, sir, here comes the lady toward my cell.
PARIS 4.1.18
Happily met, my lady and my wife!
JULIET 4.1.19
That may be, sir, when I may be a wife.
PARIS 4.1.20
That "may be" must be, love, on Thursday next. my love
JULIET 4.1.21
What must be shall be.
FRIAR That's a certain text. that's true 4.1.22
PARIS 4.1.23
Come you to make confession to the Friar1
? this Father2
JULIET 4.1.24
To answer that, I should confess to you. I would be confessing to you
PARIS 4.1.25
Do not deny to him that you love me.
JULIET 4.1.26
I will confess to you that I love him.
PARIS 4.1.27
So will you1
, I am sure, that you love me. ye2
JULIET 4.1.28
If I do so, it will be of more price value
Being spoke behind your back than to your face.
PARIS 4.1.30
Poor soul, thy face is much abused with tears. streaked
JULIET 4.1.31
The tears have got small victory by that,
For it was bad enough before their spite. the tears
PARIS 4.1.33
Thou wrong'st it more than tears with that report. you wrong your face, statement
JULIET 4.1.34
That is no slander, sir, which is a truth, lie
And what I spake, I spake it to my face. about my face
PARIS 4.1.36
Thy face is mine, and thou hast slandered it.
JULIET 4.1.37
It may be so, for it is not mine own.
[to Friar] Are you at leisure, Holy Father, now, free
Or shall I come to you at evening mass? 
FRIAR 4.1.40
My leisure serves me, pensive daughter, now. I'm free now, troubled
[to him] My lord, we must entreat the time alone. ask for
PARIS 4.1.42
God shield I should disturb devotion!— forbid, religious devotion
Juliet, on Thursday early will I rouse you+
. ye2
, wake you (with music)
Till then, adieu, and keep this holy kiss. [kisses her, exits]
JULIET 4.1.45
O, shut the door, and when thou hast done so,
Come weep with me, past hope, past cure, past help!
FRIAR 4.1.47
O Juliet, I already know thy grief. know the cause of your grief
It strains me past the compass of my wits. I'm at my wit's end
I hear thou must, and nothing may prorogue it, nothing can delay it
On Thursday next be married to this County. Count Paris
JULIET 4.1.51
Tell me not, Friar, that thou hear'st of this,
Unless thou tell me how I may prevent it!
If in thy wisdom thou canst give no help,
Do thou but call my resolution wise, 4.1.54
And with this knife I'll help it presently! now
[threatens to stab herself]
God joined my heart and Romeo's, thou our hands; you joined our hands
And ere this hand, by thee to Romeo's sealed, before my hand, that you
Shall be the label to another deed, seal, wedding contract
Or my true heart with treacherous revolt rebelliously 4.1.59
Turn to another, this shall slay them both! betrays him, knife, hand & heart
Therefore, out of thy long-experienced time long life of experience
Give me some present counsel, or behold: advice now, watch
'Twixt my extremes and me this bloody knife between my despair
Shall play the umpire, arbitrating that judge, concluding
Which the commission of thy years and art your wisdom 4.1.65
Could to no issue of true honor bring! not bring an honorable solution
Be not so long to speak! I long to die speak now, I want to die
If what thou speak'st speak not of remedy! if you offer no solution
FRIAR 4.1.69
Hold, daughter! I do spy a kind of hope, stop, see
Which craves as desperate an execution requires, act
As that is desperate which we would prevent. this desperate act, want to
If, rather than to marry County Paris,
Thou hast the strength of will to slay thyself,
Then is it likely thou wilt undertake
A thing like death to chide away this shame, avoid
That cop'st with Death himself to 'scape from it; faces death, escape
And if thou dare'st, I'll give thee remedy. give you this remedy
JULIET 4.1.78
O, bid me leap, rather than marry Paris, tell me to
From off the battlements of any2
 tower, yonder1
Or walk in thievish ways, or bid me lurk walk in dark alleyways, go
Where serpents are. Chain me with roaring bears, snakes
Or hide me nightly in a charnel-house mortuary
O'er-covered quite with dead men's rattling bones, covered up
With reeky shanks and yellow chapless skulls. stinking limbs, jawless
Or bid me go into a new-made grave 4.1.85
And hide me with a dead man in his shroud4
burial cloth
—Things that, to hear them told, have made me tremble— myself say them
And I will do it without fear or doubt,
To live an unstained wife to my sweet love. loyal 
FRIAR 4.1.91
Hold, then. Go home, be merry. Give consent wait, agree
To marry Paris. Wednesday is tomorrow.
Tomorrow night look that thou lie alone. be sure to sleep alone
Let not thy Nurse lie with thee in thy chamber. bedroom
Take thou this vial, being then in bed, little bottle, once you're in bed
And this distilling liquor drink thou off. drink all the liquid 4.1.96
When presently through all thy veins shall run soon
A cold and drowsy humor, for no pulse fluid
Shall keep his native progress, but surcease. keep beating, stop
No warmth, no breath1
 shall testify thou live'st. show you're alive 4.1.100
The roses in thy lips and cheeks shall fade rosiness
To paly4
 ashes. Thy eyes' windows fall pale grey, eyelids will close
Like Death when he shuts up the day of life. closes
Each part, deprived of supple government, part of you, unable to move
Shall, stiff and stark and cold, appear like death. rigid 4.1.105
And in this borrowed likeness of shrunk death death-like appearance
Thou shalt continue two and forty hours, forty two hours
And then awake as from a pleasant sleep.
Now, when the bridegroom in the morning comes Paris
To rouse thee from thy bed, there art thou dead. to wake you 4.1.110
Then, as the manner of our country is, custom
In thy best robes, uncovered on the bier funeral bed
Thou shalt3
 be borne to that same ancient vault shall2
, carried, tomb
Where all the kindred of the Capulets lie. family
In the meantime, against thou shalt awake, in preparation for you waking
Shall Romeo by my letters know our drift plan 4.1.116
And hither shall he come, and he and I here
Will watch thy waking3
, and that very night watch you wake
Shall Romeo bear thee hence to Mantua. take you away
And this shall free thee from this present shame, 4.1.120
If no inconstant toy nor womanish fear you don't change your mind or let
Abate thy valor in the acting it. interfere with, courage, following the plan
JULIET 4.1.123
Give me, give me! O, tell not me of fear! give me the vial
FRIAR [gives her the vial] 4.1.124
Hold. Get you gone. Be strong and prosperous here,
In this resolve. I'll send a friar with speed determined, quickly
To Mantua with my letters to thy lord. husband
JULIET 4.1.127
Love give me strength, and strength shall help afford! give me help
Farewell, dear Father!
[They exit]
ACT 4, SCENE 2
[Capulet house, almost night. LORD & LADY CAPULET, NURSE & SERVANTS]
CAPULET [handing a paper to 1st Servant] 4.2.1
So many guests, invite as here are writ. invite the guests written here
[1st Servant exits]
Sirrah, go hire me twenty cunning cooks. skilled
2nd SERVANT 4.2.3
You shall have none ill, sir, for I'll you'll get no bad ones
try if they can lick their fingers. test them to see if
CAPULET 4.2.5
How canst thou try them so? how does that test them 
2nd SERVANT 4.2.6
Marry, sir, 'tis an ill cook that cannot lick his own fingers. bad (proverb)
Therefore he that cannot lick his fingers goes not with me.
CAPULET 4.2.9
Go, be gone. [2nd Servant exits]
We shall be much unfurnished for this time. are very unprepared, event
[to Nurse] What, is my daughter gone to Friar Lawrence?
NURSE 4.2.12
Ay, forsooth. truly
CAPULET 4.2.13
Well, he may chance to do some good on her.
A peevish self-willed harlotry it is. unruly, willful tramp she is
[JULIET enters]
NURSE 4.2.15
See where she comes from shrift with merry look. look, here, confession
CAPULET 4.2.16
How now, my headstrong! Where have you been stubborn girl
gadding? wandering
JULIET 4.2.18
Where I have learned me to repent the sin learned to be sorry for
Of disobedient opposition
To you and your behests, and am enjoined commands, told
By Holy Lawrence to fall prostrate here fall to my knees
To beg your pardon. Pardon, I beseech you. forgive me
Henceforward I am ever ruled by you. from now on, will always be
CAPULET 4.2.24
Send for the County! Go tell him of this!
I'll have this knot knit up tomorrow morning! wedding knot tied
JULIET 4.2.26
I met the youthful lord at Lawrence' cell
And gave him what becomèd love I might, the appropriate amount of love
Not stepping o'er the bounds of modesty.
CAPULET 4.2.29
Why, I am glad on't! This is well! Stand up!
This is as't should be!—Let me see the County!
Ay, marry! Go, I say, and fetch him hither.— here
Now, afore God, this reverend Holy Friar, before God
All our whole city is much bound to him. obliged
JULIET 4.2.34
Nurse, will you go with me into my closet
To help me sort such needful ornaments choose what
As you think fit to furnish me tomorrow? to wear
LADY CAPULET 4.2.37
No, not till Thursday. There is time enough. wait till, there's no rush
CAPULET 4.2.38
Go, Nurse, go with her. We'll to church tomorrow.
[Juliet & Nurse exit]
LADY CAPULET 4.2.39
We shall be short in our provision. we won't have enough food or drink
'Tis now near night! almost
CAPULET Tush, I will stir about, nonsense, I'll get things going 4.2.41
And all things shall be well, I warrant thee, wife. I promise
Go thou to Juliet. Help to deck up her. get her ready
I'll not to bed tonight. Let me alone. go to bed, leave it to me
I'll play the housewife for this once.
[calling for servants] —What, ho!—
They are all forth. Well, I will walk myself out
To County Paris to prepare him up5
 up him2
 4.2.47 
Against tomorrow. My heart is wondrous light for, I am lighthearted
Since this same wayward girl is so reclaimed! has been set straight
[They exit]
ACT 4, SCENE 3
[Juliet's bedroom, that night. JULIET & NURSE]
JULIET 4.3.1
Ay, those attires are best. But gentle Nurse, clothes
I pray thee, leave me to myself tonight, leave me alone
For I have need of many orisons prayers
To move the heavens to smile upon my state, encourage, situation
Which, well thou know'st, is cross and full of sin. conflicted
LADY CAPULET [enters] 4.3.6
What, are you busy, ho? Need you my help?
JULIET 4.3.7
No, madam. We have culled such necessaries picked out everything
As are behoveful for our state tomorrow. as needed for the ceremony
So please you, let me now be left alone,
And let the Nurse this night sit up with you; stay with you
For I am sure you have your hands full all
In this so sudden business.
LADY CAPULET Good night. 4.3.13
Get thee to bed and rest, for thou hast need.
[They exit]
JULIET 4.3.14
Farewell. God knows when we shall meet again.
I have a faint cold fear thrills through my veins fainting cold fear rushing
That almost freezes up the heat of life. freezes me to death
I'll call them back again to comfort me.
—Nurse!—What should she do here?
My dismal scene I needs must act alone. dreadful 4.3.20
Come, vial.
What if this mixture do not work at all?
Shall I be married then tomorrow morning?
No, no, this shall forbid it. [takes a dagger
and puts it by the bed] Lie thou there.
What if it be a poison, which the Friar 4.3.25
Subtly hath ministered to have me dead, cunningly, administered
Lest in this marriage he should be dishonored otherwise
Because he married me before to Romeo?
I fear it is, and yet methinks it should not, I think
For he hath still been tried a holy man. always proven himself 4.3.30
How if, when I am laid into the tomb,
I wake before the time that Romeo
Come to redeem me? There's a fearful point! get me, frightening
Shall I not then be stifled in the vault, suffocated, tomb
To whose foul mouth no healthsome air breathes in, fresh 4.3.35
And there die strangled ere my Romeo comes? before
Or if I live, is it not very like isn't it likely
The horrible conceit of death and night, thoughts
Together with the terror of the place...
As in a vault, an ancient receptacle, tomb 4.3.40
Where, for these many hundred years, the bones
Of all my buried ancestors are packed;
Where bloody Tybalt, yet but green in earth, just recently buried
Lies festering in his shroud; where as they say, rotting
At some hours in the night spirits resort... haunt 4.3.45 
Alack, alack, is it not like that I, not likely
So early waking, what with loathsome smells, waking too early, awful
And shrieks like mandrakes' torn out of the earth, a plant with magic power
That living mortals, hearing them, run mad... people, go mad
O, if I wake4
, shall I not be distraught, mad 4.3.50
Environèd with all these hideous fears? surrounded
And madly play with my forefathers' joints? ancestors' bones
And pluck the mangled Tybalt from his shroud? pull
And, in this rage, with some great kinsman's bone, madness
As with a club, dash out my desperate brains? 4.3.55
O look! Methinks I see my cousin's ghost I think
Seeking out Romeo that did spit his body stab
Upon a rapier's point! Stay, Tybalt, stay! sword, stop
Romeo, I come! This do1
 I drink to thee. Romeo, Romeo, Romeo. Here's drink.
2
[She drinks then falls in bed within the curtains]
ACT 4, SCENE 4
[Capulet house, before dawn. LADY CAPULET & NURSE]
LADY CAPULET 4.4.1
Hold, take these keys and fetch more spices, Nurse.
NURSE 4.4.2
They call for dates and quinces in the pastry. are asking, fruit, pastry room
CAPULET [enters] 4.4.3
Come, stir, stir, stir! The second cock hath crowed; move it, rooster
The curfew-bell hath rung; 'tis three o'clock.—
Look to the baked meats, good Angelica. take care of
Spare not for the cost. don't be cheap
NURSE2
 Go, you cot-quean, go, LADY CAPULET+
, housewife 4.4.7
Get you to bed. Faith, You'll be sick tomorrow
For this night's watching. staying awake tonight
CAPULET 4.4.10
No, not a whit. What! I have watched ere now bit, stayed awake before
All night for lesser cause, and ne'er been sick. a woman
LADY CAPULET 4.4.12
Ay, you have been a mouse-hunt in your time, woman chaser
But I will watch you from such watching now! stay awake to keep, late nights
[Lady Capulet & Nurse exit]
CAPULET 4.4.14
A jealous hood, a jealous hood! woman
[SERVANTS enter with logs, baskets, etc.]
Now, fellow, what is there?
1st SERVANT 4.4.17
Things for the cook, sir, but I know not what.
CAPULET 4.4.18
Make haste, make haste! [1st Servant exits] hurry up
[to 2nd Servant] Sirrah, fetch drier logs.
Call Peter. He will show thee where they are.
2nd SERVANT 4.4.21
I have a head, sir, that will find out logs, good head for finding
And never trouble Peter for the matter. I won't have to
CAPULET 4.4.23
Mass, and well said! A merry whoreson, ha! good, witty fellow
Thou shalt be loggerhead! [2nd Servant exits] "blockhead"
 Good faith4
, 'tis day!
The County will be here with music straight, musicians right away
For so he said he would. 
[Music outside] I hear him near.—
Nurse! Wife! What, ho! What, Nurse, I say!
[NURSE re-enters]
Go waken Juliet. Go and trim her up! dress her
I'll go and chat with Paris. Hie, make haste, hurry
Make haste! The bridegroom he is come already!
Make haste, I say!
[They exit]
ACT 4, SCENE 5
[Juliet's bedroom. NURSE, JULIET within the bed curtains]
NURSE 4.5.1
Mistress! What, mistress! Juliet!—Fast, I warrant her, she.— fast asleep, bet
Why, lamb! Why, lady! Fie, you slug-a-bed!
Why, love, I say! Madam! Sweetheart! Why, bride!
What, not a word? You take your pennyworths now; little rest 4.5.5
Sleep for a week, for the next night, I warrant,
The County Paris hath set up his rest is determined
That you shall rest but little! God forgive me, not to let you rest
Marry, and amen.—How sound is she asleep! 4.5.10
I must needs wake her.—Madam, madam, madam!
Ay, let the County take you in your bed!
He'll fright you up, i' faith. Will it not be? startle
[opens the bed curtains]
What, dressed? And in your clothes? And down again? 4.5.15
I must needs wake you. Lady! Lady! Lady!—
Alas, alas! Help, help! My lady's dead!
O, weraday that ever I was born!— woe the day
Some aqua vitae, ho! My lord! My lady! brandy
LADY CAPULET [enters] 4.5.20
What noise is here?
NURSE O lamentable day! mournful 4.5.21
LADY CAPULET 4.5.22
What is the matter?
NURSE Look, look! O heavy day! gloomy 4.5.23
LADY CAPULET 4.5.24
O me, O me! My child, my only life!
Revive, look up, or I will die with thee! wake up
Help, help! Call help!
CAPULET [enters] 4.5.27
For shame, bring Juliet forth! Her lord is come. out here, groom is here
NURSE 4.5.28
She's dead, deceased! She's dead! Alack the day!
LADY CAPULET 4.5.29
Alack the day! she's dead, she's dead, she's dead!
CAPULET 4.5.30
Ha? Let me see her. Out, alas! She's cold! what (not laughing)
Her blood is settled, and her joints are stiff! not flowing
Life and these lips have long been separated!
Death lies on her like an untimely frost unseasonably late
Upon the sweetest flower of all the field.
NURSE 4.5.35
O lamentable day!
LADY CAPULET O woeful time! 4.5.36
CAPULET 4.5.37
Death, that hath ta'en her hence to make me wail, taken her away
Ties up my tongue, and will not let me speak. 
[FRIAR, PARIS & MUSICIANS enter]
FRIAR 4.5.39
Come, is the bride ready to go to church?
CAPULET 4.5.40
Ready to go, but never to return.—
O son! The night before thy wedding day son-in-law
Hath Death lain with thy wife. There she lies, slept
Flower as she was, deflowered by him. beautiful, her virginity taken
Death is my son-in-law; Death is my heir. 4.5.44
My daughter he hath wedded. I will die,
And leave him all: life, living, all is Death's. everything, property
PARIS 4.5.47
Have I thought long1
 to see this morning's face, looked forward
And doth it give me such a sight as this?
LADY CAPULET [all speak together] 4.5.49
Accursed, unhappy, wretched, hateful day! cursed, disastrous
Most miserable hour that e'er time saw
In lasting labor of his pilgrimage!
But one, poor one, one poor and loving child,
But one thing to rejoice and solace in, take comfort
And cruel death hath catched it from my sight! snatched her
NURSE [together] 4.5.55
O woe! O woeful, woeful, woeful day!
Most lamentable day, most woeful day, mournful
That ever, ever, I did yet behold!
O day, O day, O day! O hateful day!
Never was seen so black a day as this!
O woeful day, O woeful day!
PARIS [together] 4.5.61
Beguiled, divorcèd, wrongèd, spited, slain! cheated
Most detestable death, by thee beguiled,
By cruel, cruel thee quite overthrown!
O love! O life! Not life, but love in death! alive, but still loved
CAPULET [together] 4.5.65
Despised, distressèd, hated, martyred, killed!
Uncomfortable time, why came'st thou now comfortless
To murder, murder our solemnity? festivity
O child, O child! My soul, and not my child,
Dead art thou! Alack, my child is dead,
And with my child my joys are burièd.
FRIAR 4.5.71
Peace, ho, for shame! Confusion's cure+
 lives not there's no cure for loss / care2
In these confusions. Heaven and yourself crying and wailing
Had part in this fair maid. Now heav'n hath all, both had part, all of her
And all the better is it for the maid.
Your part in her you could not keep from death, 4.5.75
But heaven keeps his part in eternal life.
The most you sought was her promotion, wanted, material advancement
For 'twas your heaven she should be advanced. ideal that, marry well
And weep you+
 now, seeing she is advanced ye2
Above the clouds, as high as heav'n itself? 4.5.80
O, in this love you love your child so ill material concern, wrongly
That you run mad, seeing that she is well. she's in heaven (an expression)
She's not well married that lives married long,
But she's best married that dies married young. 4.5.84
Dry up your tears, and stick your rosemary place, herb for funerals &
On this fair corse, and as the custom is, weddings, corpse
In all her best array, bear her to church. clothes, carry
For though fond+
 nature bids us all lament, our emotional nature / some2
, to cry
Yet nature's tears are reason's merriment. mocked by reason
CAPULET 4.5.90
All things that we ordainèd festival, intended for the wedding feast
Turn from their office to black funeral: purpose
Our instruments to melancholy bells,
Our wedding cheer to a sad burial feast, food & drink
Our solemn hymns to sullen dirges change, funeral music
Our bridal flowers serve for a buried corse, corpse
And all things change them to the contrary. opposite
FRIAR 4.5.97
Sir, go you in, and, madam, go with him,
And go, Sir Paris. Everyone prepare
To follow this fair corse unto her grave. corpse
The heav'ns do lour upon you for some ill. frown, bad thing you've done
Move them no more by crossing their high will. anger, provoking them
[Lord & Lady Capulet, Paris, and Friar exit]
1st MUSICIAN (Simon) 4.5.102
Faith, we may put up our pipes, and be gone. put away, instruments
NURSE 4.5.103
Honest good fellows, ah, put up, put up. put away
For, well you know, this is a pitiful case. [exits]
1st MUSICIAN 4.5.105
Ay, by1
 my troth, the case may be amended. truly, situation / instrument case,
PETER [enters] could be better
Musicians, O musicians, "Heart's Ease", "Heart's Ease". 4.5.106
O, and you will have me live, play "Heart's Ease". if you want me to live
1st MUSICIAN 4.5.109
Why "Heart's Ease"?
PETER 4.5.110
O, musicians, because my heart itself plays "My Heart is Full
[of Woe]+
". O, play me some merry dump to comfort me. mournful song
1st MUSICIAN 4.5.113
Not a dump we! 'Tis no time to play now. mournful song
PETER 4.5.115
You will not, then?
1st MUSICIAN 4.5.116
No.
PETER 4.5.117
I will then give it you soundly! give it to you
1st MUSICIAN 4.5.118
What will you give us?
PETER 4.5.119
No money, on my faith, but the gleek! a sneer
I will give you the minstrel! call you "minstrels"
1st MUSICIAN 4.5.121
Then I will give you the serving-creature! call you what you are: a servant
PETER [draws his dagger] 4.5.123
Then will I lay the serving-creature's dagger on I'll knock you on the head
your pate! I will carry no crotchets! with my dagger, take no insults/notes
I'll "re" you, I'll "fa" you! Do you note me? note what I'm saying
1st MUSICIAN 4.5.126
And you "re" us and "fa" us, you note us! if
2nd MUSICIAN (Hugh) 4.5.127
Pray you, put up your dagger, and put out your wit. put away, pull, intelligence
PETER+
4.5.129
Then have at you with my wit! I will dry-beat you I'll attack you, beat
with an iron wit, and put up my iron dagger. Answer put away
me like men: [sings]
 "When griping griefs the heart doth wound,
 [And doleful dumps the mind oppress,]1
 Then music with her silver sound"—
Why "silver sound"? Why "music with her silver sound"?
What say you, Simon Catling? lute
1st MUSICIAN (Simon) 4.5.137
Marry, sir, because silver hath a sweet sound.
PETER 4.5.139
Prates! What say you, Hugh Rebeck? foolish chatter, fiddle
2nd MUSICIAN (Hugh) 4.5.140
I say "silver sound" because musicians sound for silver. play, silver coins
PETER 4.5.142
Prates too!—What say you, James Soundpost? foolish chatter,
3rd MUSICIAN (James) part of a stringed instrument
Faith, I know not what to say. 4.5.143
PETER 4.5.144
O, I cry you mercy. You are the singer. I will say I beg your pardon
for you. It is "music with her silver sound" because
musicians have no gold for sounding: [sings] don't get paid gold for playing
 "Then music with her silver sound
 With speedy help doth lend redress." [exits] make things better
1st MUSICIAN 4.5.149
What a pestilent knave is this same! miserable fool he is
2nd MUSICIAN 4.5.150
Hang him, jack! Come, we'll in here, man, we'll go in here
tarry for the mourners, and stay dinner. wait for, stay for dinner
[They exit]
ACT 5, SCENE 1
[Mantua, that afternoon. ROMEO]
ROMEO 5.1.1
If I may trust the flattering truth of sleep, believe what good dreams say
My dreams presage some joyful news at hand. predict, soon
My bosom's lord sits lightly in his throne, heart is light with joy
And all this day an unaccustomed spirit unusually good mood
Lifts me above the ground with cheerful thoughts. 5.1.5
I dreamt my lady came and found me dead,
—Strange dream that gives a dead man leave to think!— the ability
And breathed such life with kisses in my lips on
That I revived and was an emperor. 5.1.10
Ah me! How sweet is love itself possessed the love you have in reality
When but love's shadows are so rich in joy! even just love's dreams
[BALTHASAR enters]
News from Verona!—How now, Balthasar! hello
Dost thou not bring me letters from the Friar?
How doth my lady? Is my father well? 5.1.15
How fares1
 my Juliet? That I ask again, doth2
: how is
For nothing can be ill if she be well. bad, good
BALTHASAR 5.1.18
Then she is well and nothing can be ill. she's in heaven (an expression)
Her body sleeps in Capel's monument, the Capulet tomb
And her immortal part with angels lives. soul
I saw her laid low in her kindred's vault, family's tomb
And presently took post to tell it you. immediately rented a horse
O, pardon me for bringing these ill news, bad
Since you did leave it for my office, sir. make it my duty 
ROMEO 5.1.25
Is it e'en1
 so? Then I defy1
 you2
, stars!— is it really so, deny2
, my1
, fate
Thou know'st my lodging. Get me ink and paper, know where I'm staying
And hire post-horses. I will hence tonight. rent horses, leave
BALTHASAR 5.1.28
I do beseech you, sir, have patience!
Your looks are pale and wild, and do import suggest
Some misadventure. something bad will happen
ROMEO Tush, thou art deceived! nonsense 5.1.31
Leave me, and do the thing I bid thee do.
Hast thou no letters to me from the Friar?
BALTHASAR 5.1.34
No, my good lord.
ROMEO No matter. Get thee gone, 5.1.35
And hire those horses. I'll be with thee straight. right away
[Balthasar exits]
Well, Juliet, I will lie with thee tonight.
Let's see for means... O mischief, thou art swift let's see how
To enter in the thoughts of desperate men!
I do remember an apothec'ry, druggist 5.1.40
And hereabouts he dwells, which late I noted who lately I saw
In tattered weeds, with overwhelming brows, clothes, prominent
Culling of simples. Meager were his looks. gathering medicinal herbs
Sharp misery had worn him to the bones.
And in his needy shop a tortoise hung, poor 5.1.45
An alligator stuffed, and other skins
Of ill-shaped fishes; and about his shelves odd-shaped, around
A beggarly account of empty boxes, worthless collection
Green earthen pots, bladders and musty seeds, leather containers, old
Remnants of pack-thread, and old cakes of roses blocks of dried petals
Were thinly scattered to make up a show. fill up the shelves 5.1.51
Noting this penury, to myself I said poverty
"And if a man did need a poison now,
Whose sale is present death in Mantua, punishable by death
Here lives a caitiff wretch would sell it him." miserable man who would
O, this same thought did but forerun my need, foreshadow 5.1.56
And this same needy man must sell it me. poor
As I remember, this should be the house.
Being holiday, the beggar's shop is shut.—
What, ho! Apothec'ry!
APOTHECARY [enters] Who calls so loud? 5.1.61
ROMEO 5.1.62
Come hither, man. I see that thou art poor. come here
Hold, there is forty ducats. Let me have look, gold coins
A dram of poison, such soon-speeding gear some, fast-acting stuff
As will disperse itself through all the veins
That the life-weary taker may fall dead the one taking their life
And that the trunk may be discharged of breath body, exhaled
As violently as hasty powder fired gunpowder
Doth hurry from the fatal cannon's womb.
APOTHECARY 5.1.70
Such mortal drugs I have, but Mantua's law deadly
Is death to any he that utters them. sentences death, sells
ROMEO 5.1.72
Art thou so bare and full of wretchedness, poor
And fear'st to die? Famine is in thy cheeks, afraid, starvation shows
Need and oppression starveth in thy eyes, show
Contempt and beggary hangs upon thy back.
The world is not thy friend, nor the world's law. 
The world affords no law to make thee rich. offers
Then be not poor, but break it, and take this! [Offers money] break the law
APOTHECARY 5.1.79
My poverty, but not my will, consents. conscience, agrees
ROMEO 5.1.80
I pay1
 thy poverty and not thy will. conscience
APOTHECARY [offers poison] 5.1.81
Put this in any liquid thing you will
And drink it off, and if you had the strength
Of twenty men, it would dispatch you straight. kill you immediately
ROMEO [hands him the money] 5.1.84
There is thy gold, worse poison to men's souls,
Doing more murder in this loathsome world hateful
Than these poor compounds that thou mayst not sell. mixtures
I sell thee poison; thou hast sold me none.
Farewell. Buy food and get thyself in flesh. add flesh to your bones
[Apothecary exits]
Come, cordial and not poison, go with me medicine
To Juliet's grave, for there must I use thee. [exits]
ACT 5, SCENE 2
[Church. FRIAR JOHN]
FRIAR JOHN 5.2.1
Holy Franciscan Friar! Brother, ho!
FRIAR [enters] 5.2.2
This same should be the voice of Friar John.
Welcome from Mantua! What says Romeo?
Or if his mind be writ, give me his letter. if he wrote
FRIAR JOHN 5.2.5
Going to find a barefoot brother out, friar
One of our order, to associate me, our Franciscan order, to go with me
Here in this city visiting the sick,
And finding him, the searchers of the town, health officials
Suspecting that we both were in a house
Where the infectious pestilence did reign, plague had contaminated
Sealed up the doors and would not let us forth, leave
So that my speed to Mantua there was stayed. trip, stopped
FRIAR 5.2.13
Who bare my letter then to Romeo? carried
FRIAR JOHN 5.2.14
I could not send it—here it is again — back
[hands him the letter]
Nor get a messenger to bring it thee,
So fearful were they of infection.
FRIAR 5.2.17
Unhappy fortune! By my brotherhood, terrible fortune
The letter was not nice but full of charge trivial, instructions
Of dear import, and the neglecting it much importance
May do much danger! Friar John, go hence.
Get me an iron crow, and bring it straight crowbar
Unto my cell.
FRIAR JOHN 5.2.23
Brother, I'll go and bring it thee. [exits]
FRIAR 5.2.24
Now must I to the monument alone. go to the tomb
Within three hours will fair Juliet wake.
She will beshrew me much that Romeo curse
Hath had no notice of these accidents. events
But I will write again to Mantua,
And keep her at my cell till Romeo come.
Poor living corse, closed in a dead man's tomb! [exits] corpse, locked
ACT 5, SCENE 3
[Capulet tomb, late that night.
PARIS & PAGE with flowers and torch, JULIET in tomb]
PARIS 5.3.1
Give me thy torch, boy. Hence and stand aloof. go stand at a distance
Yet put it out, for I would not be seen. no instead, the torch, don't want to
Under yond yew1
 trees lay thee all along, those, lie down
Holding thy2
 ear close to the hollow ground; thine1
So shall no foot upon the churchyard tread, any footsteps in the churchyard
Being loose, unfirm, with digging up of graves, on the loose dirt from graves
But thou shalt hear it. Whistle then to me 5.3.7
As signal that thou hear'st something approach.
Give me those flowers. Do as I bid thee, go.
PAGE [aside] 5.3.10
I am almost afraid to stand alone
Here in the churchyard, yet I will adventure. [hides] take my chances
PARIS [scattering flowers over the tomb] 5.3.12
Sweet flower, with flowers thy bridal bed I strew. scatter
O woe! Thy canopy is dust and stones, bed canopy
Which with sweet water nightly I will dew, perfumed water, sprinkle
Or wanting that, with tears distilled by moans. if not that, crying
The obsequies that I for thee will keep mourning ritual
Nightly shall be to strew thy grave and weep.
[PAGE whistles]
The boy gives warning something doth approach. 5.3.18
What cursèd foot wanders this way tonight
To cross my obsequies and true love's rite? interrupt, mourning, ritual
What, with a torch! Muffle me, night, awhile. [hides] hide
[ROMEO enters with BALTHASAR with torch, pick, crowbar]
ROMEO 5.3.22
Give me that mattock and the wrenching iron. pick, crowbar
Hold, take this letter. Early in the morning here
See thou deliver it to my lord and father.
Give me the light. Upon thy life, I charge thee, I command you 5.3.25
Whate'er thou hear'st or see'st, stand all aloof, stay back
And do not interrupt me in my course. what I'm doing
Why I descend into this bed of death
Is partly to behold my lady's face, see
But chiefly to take thence from her dead finger take off from 5.3.30
A precious ring, a ring that I must use
In dear employment. Therefore hence, be gone. important purpose
But if thou, jealous, dost return to pry suspicious, spy
In what I further shall intend to do,
By heaven, I will tear thee joint by joint limb from limb 5.3.35
And strew this hungry churchyard with thy limbs! scatter
The time and my intents are savage-wild, circumstance, state of mind
More fierce and more inexorable far merciless
Than empty tigers or the roaring sea. hungry
BALTHASAR 5.3.40
I will be gone, sir, and not trouble ye2
. you1 
ROMEO 5.3.41
So shalt thou show me friendship. Take thou that. [gives money] that's how
Live and be prosperous, and farewell, good fellow.
BALTHASAR [aside] 5.3.43
For all this same, I'll hide me hereabout. all the same, nearby
His looks I fear, and his intents I doubt. [hides] intentions
ROMEO [starts forcing open the tomb] 5.3.45
Thou detestable maw, thou womb of death, stomach
Gorged with the dearest morsel of the earth,
Thus I enforce thy rotten jaws to open,
And in despite I'll cram thee with more food! in spite
PARIS 5.3.49
[aside] This is that banish'd haughty Montague arrogant
That murdered my love's cousin, with which grief
It is supposèd the fair creature died! believed, Juliet
And here is come to do some villainous shame he has come to
To the dead bodies! I will apprehend him. arrest
[to Romeo] Stop thy unhallowed toil, vile Montague! unholy work
Can vengeance be pursued further than death? worse 5.3.55
Condemned villain, I do apprehend thee! arrest
Obey, and go with me, for thou must die!
ROMEO 5.3.58
I must indeed, and therefore came I hither. that's why I came here
Good gentle youth, tempt not a desperate man!
Fly hence, and leave me! Think upon these gone; run away, deceased
Let them affright thee. I beseech thee, youth, frighten
Put not another sin upon my head
By urging me to fury! O, be gone! pushing
By heav'n, I love thee better than myself,
For I come hither armed against myself. 5.3.65
Stay not, be gone, live, and hereafter say
A madman's mercy bade+
 thee run away. bid2
: begged
PARIS 5.3.68
I do defy thy commination2
, conjurations1
: threats
And apprehend thee for a felon here. arrest, criminal
ROMEO 5.3.70
Wilt thou provoke me? Then have at thee, boy!
[They fight]
PAGE 5.3.71
O Lord, they fight! I will go call the watch! [exits] guards
PARIS 5.3.72
O, I am slain! [falls] If thou be merciful,
Open the tomb, lay me with Juliet. [dies]
ROMEO 5.3.74
In faith, I will. Let me peruse this face. look at
Mercutio's kinsman, noble County Paris!
What said my man when my betossèd soul servant, troubled
Did not attend him as we rode? I think listen to him
He told me Paris should have married Juliet. was to have married
Said he not so? Or did I dream it so?
Or am I mad, hearing him talk of Juliet, 5.3.80
To think it was so?—O, give me thy hand,
One writ with me in sour misfortune's book! you're written
I'll bury thee in a triumphant grave.—[opens the tomb] glorious
A grave? O no, A lantern, slaughtered youth, glass tower 5.3.84
For here lies Juliet, and her beauty makes
This vault a feasting presence full of light. festive hall
Death, lie thou there, by a dead man interred. buried
[laying PARIS in the tomb] 
How oft when men are at the point of death often
Have they been merry, which their keepers call jailers
A lightning before death! O, how may I uplifted spirits 5.3.90
Call this a lightning?—O my love! My wife!
Death, that hath sucked the honey of thy breath,
Hath had no power yet upon thy beauty.
Thou art not conquered. Beauty's ensign yet sign
Is crimson in thy lips and in thy cheeks, red 5.3.95
And death's pale flag is not advancèd there.— raised
Tybalt, lie'st thou there in thy bloody sheet?
O, what more favor can I do to thee
Than with that hand that cut thy youth in twain my hand, short
To sunder his that was thine2
 enemy? thy5
, cut down my life 5.3.100
Forgive me, cousin!—Ah, dear Juliet,
Why art thou yet so fair? Shall I believe beautiful
That unsubstantial Death is amorous, bodiless Death is your lover
And that the lean abhorrèd monster keeps horrible
Thee here in dark to be his paramour? mistress 5.3.105
For fear of that, I still will stay with thee, will stay forever
And never from this palace3
 of dim night
Depart again. Here, here will I remain
With worms that are thy chambermaids. O, here
Will I set up my everlasting rest, 5.3.110
And shake the yoke of inauspicious stars shake off the burden of cruel fate
From this world-wearied flesh. Eyes, look your last. body, for the last time
Arms, take your last embrace. And lips, O, you
The doors of breath, seal with a righteous kiss pure 5.3.114
A dateless bargain to engrossing Death. [kisses her] eternal contract, all-possessing
Come, bitter conduct, come, unsavory guide, escort (poison), offensive
Thou desperate pilot, now at once run on navigator, run into
The dashing rocks thy sea-sick weary bark! ship
Here's to my love! [drinks] O true apothec'ry,
Thy drugs are quick. [kisses her] Thus with a kiss I die. [dies] 5.3.120
FRIAR [enters with lantern, crowbar, spade] 5.3.121
Saint Francis be my speed! How oft tonight help me, often
Have my old feet stumbled at graves!—Who's there?
BALTHASAR 5.3.123
Here's one, a friend, and one that knows you well. it's me
FRIAR 5.3.124
Bliss be upon you! Tell me, good my friend,
What torch is yond, that vainly lends his light there, wastefully shines
To grubs and eyeless skulls? As I discern, worms
It burneth in the Capel's monument. Capulet tomb
BALTHASAR 5.3.128
It doth so, Holy sir, and there's my master,
One that you love.
FRIAR Who is it? 5.3.130
BALTHASAR Romeo. 5.3.131
FRIAR 5.3.132
How long hath he been there?
BALTHASAR Full half an hour. 5.3.133
FRIAR 5.3.134
Go with me to the vault.
BALTHASAR I dare not, sir. 5.3.135
My master knows not but I am gone hence, doesn't know I didn't leave
And fearfully did menace me with death threaten
If I did stay to look on his intents. to watch him 
FRIAR 5.3.139
Stay, then. I'll go alone. Fear comes upon me.
O, much I fear some ill unthrifty thing. evil
BALTHASAR 5.3.141
As I did sleep under this yew1
 tree here,
I dreamt my master and another fought,
And that my master slew him.
FRIAR Romeo! 5.3.144
Alack, alack, what blood is this, which stains
The stony entrance of this sepulchre? tomb
What mean these masterless and gory swords abandoned, bloody
To lie discolored by this place of peace? 5.3.148
[enters tomb]
Romeo! O, pale! Who else? What, Paris too? so pale
And steeped in blood? Ah, what an unkind hour soaked
Is guilty of this lamentable chance! grievous coincidence
[JULIET wakes]
The lady stirs!
JULIET 5.3.153
O comfortable Friar, where is my lord? comforting, husband
I do remember well where I should be,
And there I am. Where is my Romeo?
[Noise outside]
FRIAR 5.3.156
I hear some noise! Lady, come from that nest
Of death, contagion, and unnatural sleep. disease
A greater power than we can contradict oppose
Hath thwarted our intents! Come, come away! wrecked our plans
Thy husband in thy bosom there lies dead, 5.3.160
And Paris too! Come, I'll dispose of thee hide you
Among a sisterhood of holy nuns!
Stay not to question, for the watch is coming! guards are coming
[Another noise]
Come, go, good Juliet! I dare no longer stay!
JULIET 5.3.165
Go, get thee hence, for I will not away! leave
[Friar exits]
What's here? A cup, closed in my true love's hand?
Poison, I see, hath been his timeless end. eternal / premature
O churl! Drunk all, and left no friendly drop selfish man
To help me after? I will kiss thy lips. follow after you
Haply some poison yet doth hang on them perhaps 5.3.170
To make me die with a restorative. [kisses him] restoring medicine
Thy lips are warm!
1st GUARD [outside] 5.3.173
Lead, boy. Which way?
JULIET 5.3.174
Yea, noise? Then I'll be brief.
[finding Romeo's dagger] O, happy dagger! how fortunate: a dagger
This is thy sheath! [stabs herself] my heart
 There rust, and let me die. [dies]
[PAGE enters with GUARDS]
PAGE 5.3.176
This is the place. There, where the torch doth burn.
1st GUARD 5.3.177
The ground is bloody. Search about the churchyard.
Go, some of you. Whoe'er you find attach. arrest 
[Some Guards exit]
Pitiful sight! Here lies the County slain, 5.3.180
And Juliet bleeding, warm, and newly dead,
Who here hath lain these two days burièd.
Go, tell the Prince. Run to the Capulets.
Raise up the Montagues. Some others search. wake
[More Guards exit]
We see the ground whereon these woes do lie, bodies 5.3.185
But the true ground of all these piteous woes reason, pitiful
We cannot without circumstance descry. details, discover
[2nd GUARD enters with BALTHASAR]
2nd GUARD 5.3.188
Here's Romeo's man. We found him in the churchyard.
1st GUARD 5.3.190
Hold him in safety till the Prince come hither. securely
[3rd GUARD enters with FRIAR]
3rd GUARD 5.3.191
Here is a friar that trembles, sighs and weeps.
We took this mattock and this spade from him pick, shovel
As he was coming from this churchyard's side.
1st GUARD 5.3.194
A great suspicion. Stay the Friar too. very suspicious, hold
PRINCE [enters with Attendants] 5.3.195
What misadventure is so early up problem
That calls our person from our morning rest? me
[LORD & LADY CAPULET and Others enter]
CAPULET 5.3.197
What should it be that they5
 so shriek2
 abroad? is1
, shrieked+
: shout about
LADY CAPULET 5.3.198
The1
 people in the street cry "Romeo", O, the2
Some "Juliet", and some "Paris", and all run
With open outcry toward our monument. tomb
PRINCE 5.3.201
What fear is this which startles in our+
 ears? your2
1st GUARD 5.3.202
Sovereign, here lies the County Paris slain,
And Romeo dead, and Juliet, dead before,
Warm and new killed.
PRINCE 5.3.205
Search, seek, and know how this foul murder comes! learn
1st GUARD 5.3.207
Here is a friar, and slaughtered3
 Romeo's man,
With instruments upon them, fit to open tools
These dead men's tombs.
CAPULET 5.3.210
O heavens! O wife, look how our daughter bleeds!
This dagger hath mista'en, for lo, his house made a mistake, look, its sheath
Is empty on the back of Montague,
And it mis-sheathèd in my daughter's bosom!
LADY CAPULET 5.3.214
O me! This sight of death is as a bell
That warns my old age to a sepulchre. summons, tomb
[MONTAGUE & Others enter]
PRINCE 5.3.216
Come, Montague, for thou art early up
To see thy son and heir now early1
 down.
MONTAGUE 5.3.218
Alas, my liege, my wife is dead tonight. prince
Grief of my son's exile hath stopped her breath.
What further woe conspires against mine2
 age? my5
, threatens my old age
PRINCE 5.3.221
Look, and thou shalt see.
MONTAGUE 5.3.222
O thou untaught! What manners is in this, rude boy
To press before thy father to a grave? rush
PRINCE 5.3.224
Seal up the mouth of outrage for a while quiet your outcries
Till we can clear these ambiguities
And know their spring, their head, their true descent, source, origin, start
And then will I be general of your woes lead you in
And lead you even to death. Meantime forbear, death of the guilty, be quiet
And let mischance be slave to patience. be calm in the face of misfortune
[to Guards] Bring forth the parties of suspicion. suspects
FRIAR 5.3.232
I am the greatest, able to do least, biggest suspect
Yet most suspected, as the time and place circumstances
Doth make against me of this direful murder. make me look guilty, terrible
And here I stand, both to impeach and purge condemn my wrongs and
Myself condemnèd and myself excused. excuse what may be pardoned
PRINCE 5.3.237
Then say at once what thou dost know in this. immediately
FRIAR 5.3.238
I will be brief, for my short date of breath short time to live
Is not so long as is a tedious tale.
Romeo, there dead, was husband to that Juliet, 5.3.240
And she, there dead, that's2
 Romeo's faithful wife. that+
I married them, and their stol'n marriage-day secret wedding day
Was Tybalt's doomsday, whose untimely death day of death
Banished the new-made bridegroom from the city,
For whom, and not for Tybalt, Juliet pined. mourned 5.3.245
[to Capulet] You, to remove that siege of grief from her, end her grief
Betrothed and would have married her perforce promised, by force
To County Paris. [to all] Then comes she to me,
And with wild looks, bid me devise some mean upset, make a plan
To rid her from this second marriage, to get her out of 5.3.250
Or in my cell there would she kill herself.
Then gave I her, so tutored by my2
 art, mine1
, as I have studied
A sleeping potion, which so took effect
As I intended, for it wrought on her
The form of death. Meantime I writ to Romeo appearance, wrote 5.3.255
That he should hither come as this dire night tragic
To help to take her from her borrowed grave,
Being the time the potion's force should cease. effect should wear off
But he which bore my letter, Friar John, carried
Was stayed by accident, and yesternight delayed 5.3.260
Returned my letter back. Then all alone
At the prefixed hour of her waking expected
Came I to take her from her kindred's vault, family tomb
Meaning to keep her closely at my cell secretly
Till I conveniently could send to Romeo. 5.3.265
But when I came, some minute ere the time before
Of her awaking5
, here untimely lay awakening2
, tragically
The noble Paris and true Romeo dead. faithful
She wakes, and I entreated her come forth begged her to go
And bear this work of heaven with patience, 5.3.270
But then a noise did scare me from the tomb,
And she, too desperate, would not go with me, upset
But, as it seems, did violence on herself. kill herself
All this I know, and to the marriage this is all I know
Her Nurse is privy. And if aught in this aware, anything 5.3.275
Miscarried by my fault, let my old life went wrong
Be sacrificed some hour before his time my
Unto the rigor of severest law.
PRINCE 5.3.279
We still have known thee for a holy man.— we've always known you to be
Where's Romeo's man? What can he say to this?
BALTHASAR 5.3.281
I brought my master news of Juliet's death,
And then in post he came from Mantua quickly
To this same place, to this same monument. [shows a letter] tomb
This letter he early bid me give his father,
And threatened me with death, going in the vault,
I departed not and left him there. if I
PRINCE 5.3.287
Give me the letter, I will look on it. [takes the letter]— read it
Where is the County's page, that raised the watch? alerted the guards
Sirrah, what made your master in this place? come to this place
PAGE 5.3.291
He came with flowers to strew his lady's grave, scatter over
And bid me stand aloof, and so I did. stand away
Anon comes one with light to ope the tomb, soon, open
And by and by my master drew on him, soon, drew his sword
And then I ran away to call the watch. guards
PRINCE [reads the letter] 5.3.296
This letter doth make good the Friar's words, does support
Their course of love, the tidings of her death, news
And here he writes that he did buy a poison
Of a poor 'pothec'ry, and therewithal druggist, with it
Came to this vault to die and lie with Juliet.
Where be these enemies? Capulet! Montague! 5.3.301
See what a scourge is laid upon your hate, curse
That heav'n finds means to kill your joys with love! a way, children
And I for winking at your discords too disregarding your fighting
Have lost a brace of kinsmen! All are punish'd! two of my
CAPULET 5.3.306
O brother Montague, give me thy hand.
This is my daughter's jointure, for no more this handshake, wedding gift from you
Can I demand.
MONTAGUE But I can give thee more, 5.3.309
For I will raise4
 her statue in pure gold, have a statue made of her
That while1
 Verona by that name is known, is still known by that name
There shall no figure at such rate be set no figure will be as valued
As that of true and faithful Juliet.
CAPULET 5.3.314
As rich shall Romeo's by his lady's lie, I'll place a statue of Romeo by hers
Poor sacrifices of our enmity! pitiful victims of our hatred
PRINCE 5.3.316
A glooming peace this morning with it brings.
The sun, for sorrow, will not show his head. face
Go hence to have more talk of these sad things. go on
Some shall be pardoned, and some punishèd.
For never was a story of more woe
Than this of Juliet and her Romeo.
[End] 
INDEX
Sunday Prologue
1.1.1 Capulets and Montagues get into a fight; Prince stops them
1.1.118 Romeo's parents ask Benvolio about Romeo's sad mood
1.1.163 Romeo tells Benvolio he is brokenhearted
1.2.1 Capulet invites Paris to woo Juliet
1.2.47 Benvolio persuades Romeo to go to Capulet's ball
1.3.1 Juliet's mother and Nurse discuss marriage with her
1.4.1 Romeo and friends talk before the ball; Mercutio talks of dreams (Queen Mab)
1.5.1 Capulet ball begins
1.5.48 Romeo and Juliet fall in love at first sight
1.5.61 Tybalt wants to kill Romeo for crashing the party; Capulet stops him
1.5.104 Romeo & Juliet talk and kiss, then learn they are enemies
2.0.1 Prologue
2.1.1 Romeo slips away; his friends look for him
2.2.1 Romeo & Juliet exchange vows of love and plan to marry (balcony scene)
Monday
2.3.1 Friar agrees to marry Romeo & Juliet
2.4.1 Mercutio, Benvolio, and Romeo joke around and tease Nurse
2.4.164 Romeo and Nurse plan for the wedding and wedding night
2.5.1 Nurse tells Juliet the wedding plans
2.6.1 Friar, Romeo & Juliet meet to be married
3.1.1 Mercutio jokes with Benvolio
3.1.38 Tybalt comes to challenge Romeo
3.1.61 Romeo refuses to fight
3.1.74 Mercutio fights Tybalt and dies
3.1.124 Romeo fights and kills Tybalt
3.1.144 Lady Capulet demands justice; Prince banishes Romeo
3.2.1 Juliet looks forward to her wedding night
3.2.41 Nurse tells Juliet Romeo killed Tybalt and is now banished
3.3.1 Friar tries to comfort Romeo; Nurse arrives
3.3.156 They plan for Romeo to visit Juliet then flee to Mantua
3.4.1 Capulet plans for Juliet to marry Paris on Thursday
Tuesday
3.5.1 Romeo and Juliet wake as he must leave for Mantua
3.5.65 Juliet's mother tries to comfort her by cursing Romeo
3.5.108 Her mother tells her she'll wed Paris; she refuses; her father is enraged
3.5.216 Nurse advises Juliet to marry Paris; Juliet feels betrayed
4.1.1 Paris meets with Friar; Juliet arrives and evades Paris
4.1.45 Friar plans for Juliet to fake her death to avoid marrying Paris
4.2.1 Capulet advances wedding to Wednesday when Juliet feigns obedience
4.3.1 Juliet takes the sleeping potion
Wednesday
4.4.1 Capulet is preparing the wedding
4.5.1 They find Juliet and think she is dead
4.5.102 Peter and Musicians discuss a song
5.1.1 Romeo hears Juliet is dead; he plans to die by her side
5.1.61 He buys poison from an apothecary
5.2.1 Friar realizes Romeo didn't get his message
5.3.1 Paris fights Romeo and dies
5.3.84 Romeo finds Juliet and drinks the poison
5.3.121 Friar arrives; Juliet wakes and sees Romeo's body; Friar flees
5.3.165 Juliet kills herself
Thursday morning
5.3.176 Everyone discovers what happened
5.3.301 Prince condemns Montague and Capulet, who finally make peace """