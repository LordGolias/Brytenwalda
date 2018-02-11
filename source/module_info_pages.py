####################################################################################################################
#  Each quest record contains the following fields:
#  1) Info page id: used for referencing info pages in other files. The prefix ip_ is automatically added before each info page id.
#  2) Info page name: Name displayed in the info page screen.
#
####################################################################################################################
##diplomacy start+FLORISgdw070715
#cfrom .module_constants import DPLMC_DIPLOMACY_VERSION_STRING
##diplomacy end+

info_pages = [
## CC from floris 070615gdw
 ("mod_tips", "Tips", "1. You can select a character in your party as the commander for battles and control him/her to fight in battles personally. ^^2. In auto-loot menu, you can let characters select equipments automaticly, also you can talk to them to tell them how to upgrade their equipments. ^^3. Companions can also read books, and you can use auto-loot to let them to select and read readable books automaticly. ^^4. You can adjust raining and snowing possibilities in Camp options. Snowing for snowlands and raining for the other lands. ^^5. During auto-sell, items in the inventory of companions which selected as the type for sell and their prices below the auto-sell price limit will be sold to all merchants in towns or the elders in villages automaticly. Specifically foods, trade goods and books will never be sold. ^^6. To quickly move members or upgrade members in party window, hold down the control key while you left click. ^^7. All parties can reinforce their ally like Lord parties and they can join in the battle directly. ^^8. If you enounter stronger enemies and leaving some soldiers behind to cover your retreat or after escaping, the movement speed will be twice the normal speed for half an hour (game time), then it will return to normal. ^^9. The total weight of equipments will affect the archery, riding and horse archery skills. ^^10. You can order your soldiers to move to a spot by pressing and holding down the F1 key. ^^11. Horses and men move less quickly in rainy weather. ^^12. You can wait on the world map by holding down the space bar. ^^13. You can recruit new men to your party in taverns. ^^14. You can give orders to your party while in battle. ^^15. A party with high morale moves more quickly while travelling on the map. ^^16. Wounded party members will heal faster while resting in taverns. ^^17. To quickly buy and sell items in the inventory window, hold down the control key while you left click. ^^18. You can press the Backspace key during battle to bring up the command interface. ^^19. You will pay half wages to your troops while you are staying in a town or castle. Similarly, you will pay half wages to troops you garrison in a castle. ^^20. You can leave any location instantly by pressing the tab key. ^^21. You can hold down the shift key to zoom-in while aiming at distant enemies."),
## CC
##Floris begin
 ("troop_tree","Troop Tree","The troop tree is the backbone for each faction: it is the way soldiers are trained. And of course we all know that better soldiers mean the difference between victory and rotting in a cell deep in Khudan. Each faction has its own troop tree, showing the way they train their men. It is thus important to understand the thought behind these trees, the 'philosophy of troop trees'.^^When you look at the different trees, they might seem large and intimidating. But rest assured: there is a logic behind it. It all rests on three basic principles: 1. it takes a lot of time and money to train really good soldiers, 2. soldiers are people who can choose to specialise, or to widen their view, and 3. each faction has their own kind of training methods. Let's have a closer look at those three points.^^The first principle says that it takes a lot of time and money to train the best soldiers you could wish for. In Mount & Blade: Warband this is already reflected in the levels. To get a level 30 knight you'd need to train your recruit for quite a long time. The money this training costs, on the other hand, isn't that well reflected. Yes, the better a unit is, the higher the upkeep, but that's a fact ones a part of the training is completed. To get there, you need to pay for upgrades. Your better soldier needs better equipment, and training also costs a lot. These high training costs are here reflected in many upgrades you'll have to make before you have the best soldiers possible. To go from recruit to the best unit, you'll need to pay six times upgrade costs. Each step along the way I call a 'tier'. This means that each troop tree has seven 'tiers', with the first being the recruit and the last, the so-called 'top-tier unit', being the best soldier possible. So those many steps from beginning till end you see in the troop tree are actually that long training your soldier recieves in his life in your service.^^The second principle says that soldiers are people too, with their own wishes and carreer prospects. Of course, if you want to become the best possible archer in history, you'll need to train for a very long time. But what if you started the training, but discover you really don't like staying behind to shoot people: you'd rather run towards the enemy and slaughter them face to face. You could stop your archery training and start a new one, learning how to handle a sword. Of course you won't be as good as someone who had started his sword training right from the start, but you have other skills too, from your archery training. These possibilities and choices life offers, are in the troop trees reflected by the width of the tree. You could start with a certain training, but it is possible to do something completely different along the way.^^The third principle says that each faction has its own kind of training methods. In the troop trees that means that each faction has different kinds of top-tier units, and has different kinds of weaponry. Let's have a look at each of the factions:^^Swadia. Based on both England and France, they have specialized in their knights and longbows. This is reflected in the long training the recruits receive in both polearms and bows. Their pikemen aren't as well trained as their knights: most of them step upon a horse and continue to ride their lances, instead of walking with them. Also there are soldiers who wield the two-handed claymores. They are better than those pikemen, but not as good as the knights or longbowmen.^^Vaegir. Based on the early Russians, they too have specialised in strong knights. But they have learned a trick or two from the Khergit, since they can not only wield bows well too, but also mount them. Their weakness lies in footsoldiers with one-handed weapons, be it hammers or swords.^^Khergit. The Mongols of Calradia. They live and die on their horses, so it's no suprise that both their top-tier units are mounted. Early on they specialise in one-handed swords or bows.^^Nord. Based on Scandinavia and the old Vikings. They are the opposite of the Khergit: you won't find any mounted troops with the Nords. Instead they train with spears and axes, and master the art of throwing them too. There are some Nord archers, but they are considered the lowest kind of soldiers.^^Rhodok. Based on several Italian city states, such as Venice and Genoa. Like the Nord they don't have many horses in their ranks. They compensate that by training hard with their one-handed swords and a wide spectrum of different crossbows. Also they have some heavy spear training.^^Sarranid. Based on the Ottman and Egypt Islamic Empires, they know their way around with scimitars. Just like the Khergit they know how to mount archers, but they also learned to train some really heavy knights. Their uniqueness lies in their maces.^^Mercenaries. Based on the Holy Roman Empire. As a faction without land, they are for sale to anyone. Their training is not as extensive as the other factions, but their unique weaponry make them a good alternative to fill your ranks: from Swiss pikemen and German zweihanders to Teutonic knights and even crossbowmen.^^Women. Never underestimate a woman, especially those from the Holy Roman Empire. These women are like mercenaries, but with other weaponry. Bows, hammers and one-handed swords are their choices on the field.^^As you can see, the different factions all have their strengths and weaknesses, while some even heave weapons in their arsenal you won't find elsewhere. This is exactly what I meant when I said that each faction has his own training methods.^^I hope you can now understand why the troop trees are so extensive. You won't be just upgrading your units to better soldiers: you will give them a training to your liking, creating a truly unique army. You'll have to think about your men's training, giving the game an entire new dimension."),
##Floris end
##diplomacy start+
("dplmc_info", "Diplomacy Mod", "The Diplomacy mod adds some features to the game.  Most of them are accessed via your minister and several new potential employees: a chamberlain, a constable, and a chancellor.  You gain the opportunity to hire a chamberlain when you get your first village, a constable when you gain your first castle, and a chancellor when you gain your first town.  If you dismiss one of your employees, you may be able to rehire them through a well-connected spouse or one of the travellers who frequent the taverns of Calradia.^^Aside from these the mod has other features as well, which can be accessed from the Camp menu.^^This mod was built with the help of a number of individuals and builds on BW1.41 and Repolished."),
("dplmc_autoloot", "Autoloot", "Autoloot settings are managed through the camp menu.  It allows you to have your companions (named heroes, not ordinary soldiers) automatically select equipment from the loot after a battle.  In order for this feature to be enabled, one of the following must be true: someone in your party must have a Looting score of 2 or better, someone in your party must have an Inventory Management score of 3 or better, or the player himself must have an Inventory Management score of 2 or better."),
("dplmc_autosell", "Autosell", "The Autosell feature allows you to sell many items to a merchant all at once, instead of selling them one at a time.  Autosell settings are managed through the Town menu, where you can specify which types of items you want to be able to sell (e.g. you might not want to automatically sell horses) and a price limit (for example, you might not want to automatically sell any items that cost more than 200 denars).^^ There are two primary ways to use autosell.  If you speak to a Horse Merchant, Armorer, or Weapon Merchant in a town, there is a conversation option to sell items of a particular type.  Also, when visiting a town there will be an option in the Marketplace section of the menu to automatically sell your items throughout the town.^^ For people who used Autosell in other mods, note that this sells from your own inventory, according to certain rules.  Items you have equipped will never be sold, and neither will the first three items in your inventory.  After that, autosell also skips anything that it thinks might be your personal equipment (since people often have more than one set).  Regardless of whether you have them equipped, it won't sell your best bow, crossbow, armor, helmet, boots, or gloves.  If you have a bow you can use, it won't sell your best three packs of arrows, and if you have a crossbow it won't sell your best three packs of bolts.  For shields, one-handed weapons, two-handed weapons, polearms, and horses, it won't sell your best or second-best item.  Your best three throwing weapons also will not be sold.  However, items that your character is unable to use are considered fair game."),
##diplomacy end+
 ("morale", "Morale", "Morale represents the ability and willingness of the troops in a party to summon up the endurance, bravery, and discipline they need to face the stresses of battle and the march. It is not the same thing as the troops' happiness. Elite troops may grumble and whine about the hardships of campaigning -- but then stand together as one when the arrows start to fly. On the other hand, a commander who gives his men everything they want may find that they grow soft, and waiver before the enemy's charge.^^ Morale's greatest impact is on a party's behavior in battle, determining how aggressively troops engage the enemy, and how likely they are to break and run if they perceive the tide of battle turning against them. Morale also affects a party's march speed, as a less motivated party will move more slowly, as the men are not pushing themselves to their physical limit, and pause more frequently, as it waits for stragglers to catch up. Finally, a party with very low morale will start to suffer desertions.^^ Some factors that affect morale are intuitive. For example, a charismatic commander with a reputation for winning battles can infuse his or her men with a sense of confidence. Leaders who give their men well ample and varied supplies of food, and pay them on time, demonstrate that they care about their troops' welfare, and are less likely to lead them into disaster.^^ Other factors are less intuitive -- particularly those related to a party's sense of group cohesion. In a small tight-knit party, for example, men will often fight hard against daunting odds to avoid showing cowardice before their comrades-in-arms. A large party on the other hand may see its cohesion strained, as the commander has less time to supervise the men, listen to their grievances, and resolve their disputes. Frequent battles will strengthen the bonds between men, while long periods without combat will see the troops become bored and quarrelsome.^^ The morale report, accessibly by hitting the 'reports' button will give the player a sense of the factors affecting his or her men's morale."),
 ("economy", "Economy", "Towns and villages in Britannia and Hibernia need a wide variety of goods for their populations to remain healthy and productive. First in importance is food. Grain is the staple crop of Britannia and Hibernia, but people also need fat and protein in the form of meat, fish, or cheese. It takes almost as much work to preserve meat as to produce it in the first place, so salt is also in high demand. After food comes clothing: heavy wool, lighter linens, or luxurious velvet. Finally, people need the tools of their trade: ironware, pottery, leatherware, and, of course, arms, armor, and horses for war.^^Most agricultural products are produced in the villages, while artisans in the towns specialize in manufactured or artisanal goods like fabrics or ironware. Also, different resources can be found in different parts of the country. Consequently, the key to prosperity in Britannia and Hibernia is trade -- both between the villages and the towns, and between the major towns themselves.^^When trade flows, goods will be available and affordable, the population of a center will be healthy and energetic, and migrants will flock from the nearby regions. The center will produce more, consume more, and be able to contribute more in taxes to their lords. When trade dries up, towns and villages will see their workers flee to seek work elsewhere, and economic activity will drift to a stand-still. Thus, it is in the interests of rulers to protect trade routes from the hazards of war and banditry. A smart merchant, however, may want to seek out towns which have become isolated from the rest of the land, as he or she may be able to turn a tidy profit from the resulting price imbalances.^^Because villagers usually plan to take their goods to market in towns, village markets will be rather quiet places, and villagers will buy cheap and sell dear. Serious merchants will stick to the towns to make a profit, although some parties may decide to make a quick stop in a village to acquire supplies.^^A player who wants to know about the factors affecting a region's prosperity can speak to the guildmaster of the local town. Other information can be gleaned from passers-by, although they might not know very much outside of their own particular trade."),
 ("courtship", "Courtship", "You may wish to marry into one of Britannia and Hibernia's noble families. Marriage is not necessary for someone to rise in power and stature, but it does provide them with an opportunity to improve their relation with lords and establish a claim to the throne.^^Marriage requirements will be different for males and females. A male character will usually need to pursue a traditional path of courtship. He should establish a reputation in Britannian aristocratic society, get on good terms with his bride's parents or guardians, and then woo the lady according to local custom. If a player grows impatient, he may attempt to take a shortcut -- but there will be consequences in his relations with other lords.^^A male character should keep in mind that other lords will be competing with him for the affections of the kingdom's ladies. Also, a lady's tastes are unpredictable, and a player may also find that the object of his love does not love him in return. Romance, in Britannia and Hibernia as elsewhere, does not always prosper. Of course, a player may resort to other, less gentlemanly means of winning a lady's heart, but again, that will have a serious impact on his reputation.^^To get started on the path of courtship, a male player should try to get involved in the social life of the Britannian aristocracy, attending feasts and tournaments. Also, wandering troubadours and poets can serve as a useful repository of information on courtship, and keep the player up to date about the latest gossip.^^Female characters can also marry -- but they should keep in mind that Britannian society is very traditional, and, as adventurers, they have chosen a very unconventional path for a woman. A female character may have to look for a while to find a lord who is open-minded enough to marry her.^^On the bright side, a female character does not have to go through the elaborate rituals of courtship, and she also may gain more from a marriage than her male counterpart. For a woman adventurer, marriage can be a quick path to power -- and an unscrupulous character may be able to use her husband as a tool of her political ambitions."),
 ("politics", "Politics", "The realms of Britannia and Hibernia, although they represent different cultures, all adhere to the same basic political system: feudalism. Feudalism is based on the relationships between individuals: the oaths of loyalty given by a vassal to his or her liege. In exchange for this oath, the vassal will usually receive a fief, a parcel of land whose income will be used by the vassal to raise troops to support the liege in time of war. A liege also has an obligation to protect his vassals, and to treat them justly.^^This is how it works in theory, anyway. In practice, vassals will not always work in their factions' interests, particular as they are often quarreling with one another. Nobles have different personalities, and sometimes those personalities clash. Or, perhaps two nobles were once friends, but fell out over in the aftermath of a setback or a defeat -- or because they both were wooing the same lady. Jealousies will also surface as they vie for the favor of the king -- perhaps over newly conquered lands, or over who will be given the coveted office of marshal, the lord in charge of organizing large-scale campaigns.^^When one realm in Britannia and Hibernia makes war on another, the political unity of the each kingdom is as important as the quality or number of its soldiers in determining the outcome. In a cohesive kingdom, nobles will join together in a large force to sweep their opponents before them. In a kingdom divided by petty quarrels, lords will fail to respond to the marshal's summons, or drift away to attend to their own business if a campaign is not going well. A faction's political cohesion will also impact warfare when campaigns are not in progress. In a divided faction, lords will be less likely to join together on raids and patrols, and come to each other's defense.^^If it seems self-defeating for nobles to bicker and quarrel when the enemy is just over the horizon, keep this in mind -- ultimately, a noble's loyalty goes not to a particular faction or culture, but to himself and to his family. If a noble fears that his faction is collapsing, or if he is being neglected by his liege, he can usually find a reason to withdraw his oath of allegiance, and change sides. Players should keep this in mind, as they may find that there are opportunities to turn discontented former enemies into allies."),
 ("character_backgrounds", "Character_Backgrounds", "A player character in Britannia and Hibernia may choose to come from a variety of social backgrounds. This choice will affect not just his or her starting skills and equipment, but also the course of his or her career as an adventurer.^^War and politics in Britannia and Hibernia are traditionally dominated by male aristocrats. A nobleman player character may find that he is invited into this 'old boys' club' fairly quickly, but women and commoners may face a few extra hurdles on the way. If you choose to start the game as a male nobleman, you can think of it as the 'easy' setting. Starting as a noblewoman or a male commoner is somewhat more difficult, and starting as a female commoner is probably the most challenging way to begin a game.^^However, women have some starting advantages. Simply by taking up arms, a female warrior will draw attention to herself, and she may find that she can build up her reputation faster than a male. Also, it is traditionally easier for a woman to marry up the social ladder than it is for a man, and a woman may find she can gain more from a strategic marital alliance than her male counterpart.^^Finally, keep in mind that the game does not place any limits on the upward mobility of characters based on their background. Noble or common, male or female, married or unmarried -- anyone can rise to become ruler of all Britannia and Hibernia, if they are sufficiently brave, lucky, or resourceful."),
 ("military_campaigns", "Military Campaigns", "When kingdoms in Britannia and Hibernia go to war, their armies have two basic offensive options. They can try to attack villages and lay waste to the countryside, damaging their enemy's prestige and economy. Or, they can try to seize and hold castles or towns, taking territory This second option can involve long, bloody sieges, but will yield more decisive results.^^It is important to note that the realms of Britannia and Hibernia do not field standing armies, which remain in the field as long as the ruler desires. Rather, Britannian realms are protected by feudal levies comprised of the major nobles and their individual retinues.  Sometimes, these nobles launch their own private attacks into enemy territory, but the most decisive events will usually take place when the great hosts are assembled. The kingdom's marshal, a noble appointed by the king, will summon the host before the campaign and lead them out to battle. However, he should be careful not to keep them in the field too long. Otherwise, the host will begin to disintegrate, as the vassals drift off to pursue their own business, and the army will be vulnerable to a counter-attack.^^For this reason, the rhythm of wars in Britannian and Hibernia often resemble the rhythm of a duel between two individual combatants. One side will gather its strength and seek to land a blow against the enemy's territory. If the marshal spends too little time gathering the vassals, he may not be able to do any real damage. If he spends too much time, then the campaign may end before it has even begun. A large realm will have an advantage over a smaller one, just as a brawny combatant has an edge over a smaller foe, but a realm's political cohesion can also be a factor, just as a fighter with great stamina can outlast her opponent. Sometimes, the armies of two realms will meet head on, resulting in a major battle in which both numbers and morale will decide the outcome.^^Kingdoms will have imperfect intelligence about their enemies. Attacking lords will need to frequently scout enemy territory to determine which fortresses may be vulnerable. An army defending its homeland will benefit from the alarms raised by castles and towns, which broadcast intelligence about enemy movements in the area. Such intelligence will be imprecise, however, particularly when it comes to numbers. A defending force which sets out to raise a siege or rescue a village may be able to overwhelm an unprepared attacker -- or it may miscalculate, and find that it is the one to be overwhelmed. Attackers, in turn, must be careful how far they advance into enemy territory, with aggressive marshals venturing further than cautious ones.^^Players will be expected to join in their faction's military campaign, either by joining the host, or by scouting ahead into enemy territory. Some players may find that their realm's marshal is too cautious, or too aggressive, for their tastes. In this case, they can intrigue with other lords to try to replace the marshal, or build support to become the marshal themselves.^^Most wars are of limited duration. A king who goes to war will, for the sake of honor, feel obligated to pursue the conflict for a short while. However, unless he is soundly beating his enemy. he may soon start looking for a way out of the conflict, lest he leave himself vulnerable to an attack by a third party. Britannia and Hibernia's rulers are keenly aware that today's ally may be tomorrow's enemy, and vice versa."),
#chief anadido
 # for KLABAUTERMANN
  ("naval_warfare", "Naval Warfare", "You lead your men to battle on longboats. You are the captain of the first ship. You must give commands. Your other ships will be commanded by one of your men. ^^With the 'up' and 'down' keys you give your crew commands to change the rowing speed. ^^With the 'right' and 'left' keys you give your  helmsman commands to change the rudder direction. ^^With the 'enter' key you give command to lower or set the sail. ^^With the 'right shift' key you ask your tax man for a situation report.^^With the 'K' key you decide which boats you would like to board.^^With the 'J' key you decide if you want to land.^^With the 'backspace' key you can change your point of view.^^You know where south is when you consider the position of the sun and the time of day."),
 ("prisioner_system", "Prisioner System", "The skill 'prisoner management' is eliminated from Brytenwalda, as it seems unrealistic to manage the number of prisoners in terms of a skill. In Brytenwalda the number of prisoners that the player can have depends on the size of his/her army. That is, the more troops able to keep guard, the more prisoners it can carry."),
 ("ambush", "Ambush", "The ambushing skill allows you to set up ambuhes. From the camp game menu, choose to set up an ambush. You will then have feelings about your ambush, and if you are really attacked,^\
you will have the choice to launch the ambush. Ambushes can have devastating positive or negative effects."),
 ("sneaking", "Sneaking", "The sneaking skill allows you to sneak. From the camp game menu, choose to sneak. Sneaking will reduce your speed.^\
However, if you are the attacker, you might have, according to you sneaking check, some combat bonus (but not as great as in an ambush."),
 ("entrenchment","Camp Entrenchment", "  When your army sets up camp for the night, you are given the option to entrench your camp site. An entrenched camp site is a temporarily fortified position using terrain and pickets as a defensive barrier. Armies composed mostly of cavalry units will get little benefit from entrenching. Armies comprised mostly of foot soldiers will find that entrenchment will give them a significant advantage over cavalry units. Soldiers very much dislike digging holes and planting pickets, so you will suffer a small morale penalty when choosing this option.^^ If you choose not to entrench your camp site, you will be at a disadvantage if attacked while camping. Your camp may be over run and plundered. Items in your inventory may be looted or destroyed in the battle. An entrenchment that has not been over run recieves the benefit of multiple ammunition reloads for the troops. A normal camp site gets no such benefit.^^  In order to entrench your position you will need tools, time, and skill. Tools can be purchased at many of the towns in Calradia, and one set must be in your inventory in order to entrench. The time required to entrench is based upon the number of soldiers in your army and your parties skill in engineering. A small band of warriors with no skill in engineering will take days to entrench a camp site. An army of 30 or more with a few points in engineering can accomplish this in just a few hours.^^ When you complete the entrenchment, a circle of pickets will surround your camp. This entrenchment will remain in place for approximately three days after leaving the entrenchment. You can leave and return to the entrenchment during this time without having to do any more digging or planting of pickets, thus avoiding any morale penalty. This makes an entrenched site an excellant base of operations for sieges or incursions into enemy territory."),
 ("siege_warfare","Brytenwalda Siege Warfare", " One of the things we missed in Warband was completely realistic siege warfare. Brytenwalda exploits this to the fullest. Now when the player besiege a settlement two paths can be taken to subjugate the place: by debilitation (hunger, diseases ...) and by assault.^^\
In the first case, the player's mission is to encircle the settlement (you need 200 or more men) and prevent it from receiving supplies or reinforcements. At the same time various actions can be performed to undermine morale, spread disease or destroy food reserves of the settlement. This type of action will take longer, but also prevent a large number of casualties.^^\
In the second case direct action is taken, provided assault equipment is available (ladders, battering ram, ramps, mantlets ...) or offensive actions (wearing down the defenders, burning their houses and walls ...). This is when the player feels ready to launch a full-scale assault to conquer the settlement. This type of action has the advantage that the place can be vanquished in a short amount of time, but usually at a very high cost of lives.^^\
In addition to the above, a new system of assault involving both types of siege tactics is also available. When the settlement has a port, the player may equip a fleet and block the port. The player can then choose to continue the siege until the surrender by debilitation, or lead an assault by sea.^^\
The complexity and characteristics of the new siege system is long, and the best thing is to discover and develop strategies for yourself. Welcome to Realistic Siege Warfare."),
 ("battle_wounds","Battle Wounds", "Death/Wound/Recovery upon knockout scheme:^^\
Upon getting knocked out in battle one of four things will happen: Complete recovery (70%), Light Wound (20%) and Severe Wound (10%).^^\
The result is modified by your skill levels in Ironflesh. Every point in that skill moves you up 1% on the scale of outcomes.^\
Charisma scores, represting luck, do the same. Every point in Charisma above 10 moves you up 1%. If your Charisma is below 10, you are considered to be unlucky and will move down on the scale by 1% for every point lacking to reach 10.^^\
Wounds take one month to heal, one day sooner for each healing skill level, so that with 10 wound treatment, first aid and surgery they will heal in one day.^^\
Suffering the same wound before the first one has healed will make effects of the first one permanent. For example, if you get broken arm, and one week later, before it heals, broken arm again, when they heal you will recover the penalties of only one, the others will stay permanent."),
#chief anadido
 ("brytenwalda_formations", "Battle Keys and Orders",
"Formations: active with F4 in Battle, then:^\
F4 - form ranks,^\
F7 - form squares,^\
F5 - form shieldwall,^\
F6 - form wedge,^\
F8 - break the current formation,^^\
Memorize Division Placement and Formation: active with F2 in Battle, then:^\
F7 - memorize relative position to player and formation,^\
F8 - revert to default relative position to player and formation,^^\
Orders: active with F5 in Battle, then:^\
F5 - Order 'use onehand weapons',^\
F6 - Order 'use twohands and polearms weapons',^\
F7 - Order 'use ranged weapons',^\
F8 - Order 'use,quit shields',^^\
Hold-F1 on an enemy division - and the divisions you have selected will attack it,^^\
Others:^\
key U - Battlecry (encourage your wounded troops's),^\
key B - Warcry (scare away enemies surrounding you),^\
key T - Use Fire (your troops use fire. For sieges and ship battles only),^\
key F6 - Skirmish order (your troops avoid enemy, moving away when enemy approaches),^\
key F9 - Order beginning or ending volley fire for archers,^\
Right Click + Left Click - Shield Bash."),
# chief time line
 ("timeline_britannia", "Timeline 597 to 636",
"597 - The Roman brand of Christianity is brought to Britain for the first time by St. Augustine, the missionary sent from Pope Gregory to convert the Saxons. Augustine lands in Kent and is welcomed by King Aethelbert whose Frankish Queen is already a Christian practicing at her church of St. Martin's, Canterbury. Augustine converts Aethelbert and his court to Christianity and founds a monastery at Canterbury. Commencement of the erection of a monastery at St. Augustine's, Canterbury, built from the Roman ruins of the old city. Death of King Ceol of Wessex. He is succeeded by his brother, Ceolwulf.^\
------^^\
598 - Kings Mynyddog Mwynfawr of Din-Eidyn & Cynan of Gododdin ride south to fight King Aethelfrith's Bernician army against enormous odds at the Battle of Catterick. The British are victorious. Probable expansion of North Rheged to fill the vacuum left in North Yorkshire. ^\
------^\
602 - St. Augustine of Canterbury meets with the Welsh Bishops at Aust near Chepstow. He accuses them of acting contrary to Church teachings, failing to keep Easter at the prescribed Roman time and not administering baptism according to the Roman rite. He also insists that they help in the conversion of their enemy, the Saxons, and look to Canterbury as their spiritual centre. The Welsh tactfully decline. Augustine is proclaimed Archbishop of Canterbury and commences the erection of his stone-built Cathedral.^\
------^^\
604 - The Welsh Bishops meet for a second time with St. Augustine of Canterbury. He neglects to rise to greet them, lectures them again and insists they submit to him. The Welsh send him packing. They refuse to recognise the authority of a church within their enemies' territory under such a disrespectful bishop. The See of Rochester is established and Justus appointed its first bishop. Death of King Sledda of Essex. He is succeeded by his son, Saebert. King Saebert is persuaded to convert to Christianity through the intervention of his uncle, King Aethelbert of Kent. The See of Essex is founded. King Aethelbert of Kent founds the cathedral church of St. Paul in London. St. Mellitus is appointed the first Saxon Bishop of London (& Essex). King Aethelfrith of Bernicia invades Deira and kills its king, Aethelric. Prince Edwin, son of the late King Aelle of Deira (and possibly nephew of King Aethelric) flees to the Court of King Iago of Gwynedd. Aethelfrith marries King Aelle's daughter, Acha, and takes the kingdom.^\
------.^\
605 - Birth of Prince (later King) Oswald of Bernicia. Death of Bishop Augustine of Canterbury. He is buried in St. Augustine's Abbey, Canterbury and later revered as a saint. He is succeeded by St. Laurence of Canterbury.^^\
------ ^\
606 - Death of King Pybba of Mercia. He is succeeded by his kinsman, Ceorl.^\
------^^\
611 - Death of King Ceolwulf of Wessex. He is succeeded by his nephew, Cynegils. King Cynegils shares power to some extent with his eldest son, Cwichelm, who may have been given Upper Wessex.^\
------.^\
613 - King Aethelfrith of Bernicia invades Gwynedd in order to route out his old enemy, King Edwin of Deira. A united British force (Gwynedd, Powys, Pengwern and Dumnonian warriors) clashes with his army at the Battle of Chester. King Iago of Gwynedd and King Selyf Sarffgadau of Powys are both killed but the victor is unclear. The Battle of Bangor-is-Coed follows in quick succession. King Bledric of Dumnonia is killed in the fighting and 1000 monks are massacred by the Northumbrians. King Edwin of Deira flees to the Court of King Raedwald of East Anglia. Birth of Prince (later King) Oswiu of Bernicia. The stone Abbey Church at St. Augustine's Abbey, Canterbury is completed and dedicated to St. Peter and St. Paul.^^\
------.^\
614 - King Cynegils & his son, Prince Cwichelm, of Wessex invade Dumnonia and defeat the local army (possibly under a King Clemen) at the Battle of Bindon. Birth of Princess (later Abbess & Saint) Hilda of Deira.^\
------.^\
c.615 - King Aethelfrith of Bernicia visits King Raedwald of East Anglia at Rendlesham and persuades him to hand over the former's old enemy, King Edwin of Deira. In return, Raedwald is promised rich rewards, yet war is threatened if he fails to comply. Raedwald's wife however, reminds him of his obligations as Edwin's protector and the King begrudgingly declines the offer. King Edwin of Deira marries Princess Cwenburga, daughter of King Ceorl of Mercia.^^\
------.^\
616 - King Edwin of Deira, with the help of King Raedwald of East Anglia, conquers Northumbria at the Battle of the River Idle. King Aethelfrith of Bernicia & Deira is killed in the fighting and his children are forced to flee north. His heir, Prince Eanfrith, seeks refuge with his mother's family, probably in Gododdin, and then moves further north into Pictland; Princes Oswald, Oswiu and others escape to Court of King Eochaid Buide of Dalriada where they are converted to Christianity by the monks of Iona. Death of Kings Aethelbert of Kent and Saebert of Essex. The former is succeeded by his pagan son, Eadbald, who promptly marries his step-mother, in accordance with pre-Christian custom. King Eadbald loses overlordship of Essex, where the new kings, Saebert's sons, Sexred, Saeward and Sexbald, throw out the Christian missionaries and return to paganism. Bishop (& Saint) Mellitus of London (& Essex) flees with Bishop Justus of Rochester to France. King Eadbald of Kent is persuaded to convert to Christianity by St. Laurence, Archbishop of Canterbury.^^\
------.^\
617 - King Edwin of Deira invades and conquers Elmet. King Ceretic of Elmet is killed in the fighting. Death of King Raedwald of East Anglia. He was probably buried in the Great Ship discovered in the Royal East Anglian Cemetery at Sutton Hoo. Shortlived succession of his brother, Eni.^^\
------.^\
618 - Raedwald's son. Eorpwald, takes the East Anglian throne from his uncle, King Eni.^^\
------.^\
619 - Death of Archbishop Laurence of Canterbury. He is buried at St. Augustine's Abbey, Canterbury and is later revered as a saint. He is succeeded by St. Mellitus.^^\
------.^\
620 - The church of St. Mary is built at the Royal Abbey complex of St. Augustine's, Canterbury.^\
------.^\
c.620 - Angles probably under King Edwin of Deira invade South Rheged, and expel King Llywarch Hen who flees to Powys. Edwin's armies also move north into Southern Strathclyde and Gododdin. Prince Eanfrith, heir of Bernicia, marries a Pictish Royal Princess and fathers Prince (later King) Talorcan (I) of the Picts.^^\
------.^\
c.623 - King Edwin of Deira is baptised by Prince Rhun of North Rheged, according to the Historia Brittonum. This was probably at the Royal Court of Gwynedd. He soon relapses back to paganism.\
------.^\
624 - Death of Archbishop Mellitus of Canterbury. He is buried at St. Augustine's Abbey, Canterbury and is later revered as a saint. He is succeeded by Bishop (& Saint) Justus of Rochester.^^\
------.^\
625 - King Edwin of Deira marries Princess Ethleburga of Kent. As a Christian, she brings her personal chaplain, Paulinus, north with her. St. Paulinus has already been consecrated Bishop of York. With the help of Pope Boniface, the new Queen encourages her husband to convert to Christianity.^\
------.^\
626 - Death of King Ceorl of Mercia. He is succeeded by Penda, son of his predecessor. Prince Cwichelm of Wessex sends an assassin to murder King Edwin of Deira. Edwin is saved from the assassin's dagger by the timely intervention of one of his thanes who is killed in the process. Edwin's daughter, Eanflaed, is born the same night and he promises to give her for baptism to St. Paulinus, if he is victorious over the instigator of this crime. Edwin discovers Cwichelm's treachery and marches on Wessex. Prince Cwichelm and his father, King Cynegils of Wessex, march north to meet the Northumbrians at the Battle of Win Hill & Lose Hill, possibly with the aid of King Penda of Mercia. Despite their army's superior numbers, the Wessex duo are defeated and flee south. Edwin keeps his promise to St. Paulinus.^^\
------.^\
c.626 - The rivalry between King Edwin of Deira and King Cadwallon of Gwynedd, which has grown since childhood, reaches a climax. Edwin invades the Isle of Man and then Anglesey. Cadwallon is defeated in battle and is besieged on Puffin Island. He eventually flees to Brittany.^\
------.^\
627 - St. Paulinus converts King Edwin of Deira back to his lapsed Christianity at the Royal Court of Yeavering. The King is baptised in Paulinus' proto-Cathedral in York and persuades his sub-monarch, King Eorpwald of East Anglia to follow suit. Death of Archbishop Justus of Canterbury.^\
------.^\
c.627 - Possible building of the Western section of the Wansdyke, by King Cynegils of Wessex, in an attempt to counter aggression from King Penda of Mercia.\
------.^\
628 - King Cynegils and his son, Prince Cwichelm, of Wessex clash with King Penda of Mercia at the Battle of Cirencester. Cynegils' son, Cenwalh, may have married King Penda's sister as part of the subsequent peace treaty by which the Mercians take control of the area. King Penda probably establishes the sub-Kingdom of the Hwicce at this time. Anti-Christian uprising in East Anglia. King Eorpwald is killed by one Ricbert, and his half-brother, Sigebert, flees to France. Ricbert takes the throne. The exiled Prince Oswald of Northumbria accompanies King Connad Cerr of Dalriada to Ireland to fight against Maelcaich and the Irish Cruithne at the Battle of Fid Eoin.^\
------.^\
629 - St. Paulinus meets Blecca, the Praefectus Civitatis of Lincoln, and converts him to Christianity.^\
------ ^\
c.630 - King Penda of Mercia besieges Exeter (possibly held by King Clemen of Dumnonia). King Cadwallon of Gwynedd lands nearby, from his Deiran imposed exile in Brittany. He negotiates an alliance with King Penda of Mercia and a united British and Saxon force moves north to re-take Gwynedd. The Deirans are defeated at the Battle of the Long Mountain and Cadwallon chases them back to Northumbria. The British ransack Northumbria and bring the kingdom to its knees. St. Felix arrives in Britain from Burgundy with the intention of evengelising the Angles. He stays a while at Canterbury.^\
------ ^\
631 - Death of King Ricbert of East Anglia. The half-brother of his predecessor, King Eorpwald, returns from exile in France and takes the throne as the Christian King Sigebert. With the new King's encouragement, St. Felix is sent by Archbishop Honorius of Canterbury to evangelise his people. St. Felix establishes his see at Dunwich.^\
------ ^\
c.631 - King Edwin of Deira re-fortifies the City of York, probably including the building of the so-called Anglian Tower.^\
------ ^\
632 - The West Saxons cross into Wales and defeat King Idris of Meirionydd on the Severn.^\
------ ^\
633 - King Edwin of Deira and his Northumbrian army meet the British, under King Cadwallon of Gwynedd, in the Battle of Hatfield Chase. King Edwin is killed in the fighting and Cadwallon is victorious. Edwin's cousin, Osric, succeeds to the throne of Deira and Prince Eanfrith of Bernicia returns from Pictland to claim his rightful crown. Both are pagans. St. Paulinus, Bishop of York, flees south and is made Bishop of Rochester. Cadwallon is later besieged at York by King Osric. The former is again victorious.^\
------ ^\
634 - Despite suing for peace, King Cadwallon of Gwynedd slays both King Eanfrith of Bernicia and Osric of Deira rather than negotiate with them. Eanfrith's half-brother, Oswald succeeds, as son of Aethelfrith of Bernicia and Acha of Deira, to a united Northumbria. He is given a force of men (including monks from Iona) by King Domnall Brecc of Dalriada and marches south to claim his inheritance. He clashes with King Cadwallon of Gwynedd at the Battle of Heavenfield. Despite having superior numbers, Cadwallon is killed, and King Oswald victorious. The former Queen Ethelburga of Deira packs up her infant sons and step-grandson and flees to France for fear that, as offspring of her husband, King Edwin, Oswald will have them murdered. The Deiran Royal Court at Yeavering is probably abandoned at this time. Oswald re-introduces Christianity to Northumbria, though James the Deacon is still ministering to the people of Swaledale. The chief among the monks who accompanied the King from Dalriada attempts to convert the Northumbrians, but meets with little success. Oswald calls on Iona to send an evangelical Bishop. King Sigebert of East Anglia retires to the monastery of Burgh Castle and entrusts the kingdom to his cousin, Egric, who had already been deputising in part of the country. St. Birinus arrives as a bishop from Genoa to convert the people of Mercia. He, however, decides to halt in Wessex instead. He preaches to King Cynegils of Wessex near Cholsey. Birth of St. Cuthbert in Tweedale and St. Wilfred in Northumbria.^\
------ ^\
635 - King Penda of Mercia aims to gain control of Middle Anglia and therefore attacks his rivals in East Anglia. Ex-King Sigebert is forced to leave his monastery in order to join King Egric of East Anglia in battle against the invaders. Sigebert and Egric are both killed in the fighting. Sigebert is later revered as a saint. Egric's brother, Anna, succeeds to the East Anglian throne. St. Aidan, Bishop of Scattery Island, arrives to evangelise Northumbria and founds the Bishopric and Priory of Lindisfarne. Under pressure from King Oswald of Northumbria, King Cynegils of Wessex, is persuaded to allow St. Birinus to convert him to Christianity. Cynegils' eldest son, Cwichelm, resists. Cynegils is baptised at Dorchester-on-Thames and gives Birinus the town for his cathedral. Birinus is made the first Bishop of Wessex. Oswald acts as godfather and agrees to enter into a strategic alliance with Wessex against Mercia. The agreement is cemented by the marriage of King Oswald to King Cynegils' daughter, Princess Cyniburg.^\
------ ^\
c.635 - St. Finnian and St. Aebbe, half-sister of King Oswald of Northumbria, found the monastery of Coldsbury at St. Abbs.^\
------ ^\
636 - St. Birinus converts Prince Cwichelm of Wessex to Christianity. The latter dies soon afterward. He is supposedly buried at Scutchamer Knob in East Hendred.^\
------ ^\
c. 636 - Brytenwalda mod begin. It is your turn of do History.^\
------ ^\
Source: http:,,www.britannia.com,history,saxontime.html . We had guard actual names here for your comprension. In Brytenwalda mod, you can see them like old name was."),
# chief -
 #chief historical battle system
 ("battle_system", "Dark Age Battle System.",
"The new fight system of BRYTENWALDA is the result of a deep study to reach the maximum offered by the Warband engine.^^\
The starting idea was to make the AI an enemy difficult to defeat, and also to make the battles more complex and fun, not for arcade players but for strategy lovers. We have tried to accomplish these requirements by studying manuals of battles and strategies of the historical period, as well as the different classical sources that make reference to this points. Also we added the experimental research of clan mates and recreation world in the exercise of throwing javelins and using slings. No animal suffered and no public harm was done during those tests.^\
Realism was intended to be the way and the transport behind it, fighting the limitations of the engine with historical situations for the generals and Lords of War in this period.^\
Features:^^\
In principle the movement of our army will vary much more depending on the terrain and also depending on the man. A heavy infantryman should be very slow, but the light infantryman should move quickly and easily.^\
Each unit has been reworked in different aspects. Heavy infantry will behave as heavy infantry, with good defense, but slower in attack and manoeuvring. The same for the rest of the units.^\
The heavy infantry in history has generally been used as an element of shock, with limited tactics. I speak of the heavy infantry especially because at this time it was the core of the armies. His way forward was to advance, throwing javelins or darts, form a shieldwall and charge. Defensively he held the enemy while the cavalry, light infantry or other heavy infantry won the flanks of the enemy. Offensively he fall upon the enemy, colliding and bleeding. Battles here were won from moral, not from causalities, never forget that.^^\
And men were not fighting for hours. A man can fight with maximum effort for a time of 10 to 15 minutes, before being exhausted. So there was a relay system, for example.^\
Several parameters have been taken into account, such as the lethality and reaction time of each weapon, and they are now different. A knife can be terribly rapid, but not very dangereous, mainly depending on the armour of the enemy it faces. It cannot be the same thing trying to trespass a chainmail or gutting an almost nude slinger. Each weapon will give advantages and disadvantages. A heavy sword will give a certain advantage in charges, but is less efficient in close melee fighting. A short sword on the contrary, is not the best weapon to charge with, but is very lethal in close combat.^\
Projectiles are another point drastically transformed in Brytenwalda. These units are no longer machine guns, casualties will depend more on the position related to the objective and we have tried to adjust casualties to the data obtained from ancient-medieval battles. They are a good tactical element if used properly, as they can reduce the morale of the enemy, making charges more efficient.^\
Morale: There are no men whom fear does not touch. Fighting to death is very epic, but not realistic at all. In Brytenwalda the soldiers will be unpredictable. They can fight as lions or, more probably, rout quickly in a difficult moment. Battle now requires a strong organization in the troops or you will falter.^\
If you want to bring veterans to battle, you will have to invest money as they are expensives. It is your choice, either a small high quality force or a large rabble mob.^\
In any case our goal is that the battle will be won by the best general, that knows how to take advantage of his troops, their morale and the terrain in the best way, not by the general with the most powerful army. Superhuman units have disappeared."), 
 ("toponimia_brytenwalda", "Toponyms ancient and actual name",
  "The Great Brytenwalda Dictionary of Toponyms, by Dante Borgia and Iskar.^^\
'A'^^\
Aber Lleu = Ross Low^\
Abercrdf = Abergavenny^\
Aberlessic = Aberlady^\
Abermynwy = Monmouth^\
Aberystwyth = Still the same^\
Achadh Chuinnire = Achonry^\
Achadh Fharcha = Agheragh^\
Ached Bou = Aghaboe^\
Ached Fobuir = Aghagower^\
Ad Candida Casam = St. Ninian^\
Ad Cluanan = Clunie, Aberdeenshire^\
Ad Gefrin = Ancient Palace complex now archaeological site^\
Aebbercurning = Abercorn^\
Aegelesburh = Aylesbury^\
Aemethyll = Ampthill^\
Aewiue = Possibly an insignificant village greater area with different name,  or no longer exists^\
Aidhne = Area south of Galway. Aidhne is coextensive with the present diocese of Kilmacduagh^\
Aileach = Grianan of Aileach^\
Aillinn = Dun Ailinne^\
Alne Ceaster = Alcester^\
Alwric = Aldridge^\
Altitudo Mach = Armagh^\
Amwythig = Shrewsbury^\
Anava = Annan^\
Aporcrosan = Applecross^\
Ard Breacain = Ardbraccan^\
Ard Eachadha = Ardaghy^\
Ard Ladhrann = Ardamine^\
Ardea = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Arderydd = Arthuret^\
Ardudwy = Area in North-West Wales^\
Art Muirchol = Ardnamurchan^\
Ath Berchna = Connacht, north-west of Croohan, near Bellanagare; OR it may be for Ath Bercha, in East Roscommon^\
Ath Cormac = Ford of Cormac^\
Ath Mor = Athlone (An Sean Ath Mor to be precise)^\
Ath an Tearmainn = ancient place in county Roscommon, mentioned in synodal texts^\
Ath na Foraire = South Armagh^\
Athfolta = Atholl^^\
'B'^^\
Badun = Somerset^\
Baile Loch = Strangford^\
Banesbyrig = Banbury^\
Bangor Is Coed = Bangor on Dee^\
Bartun = Barton^\
Barum = Barum Top^\
Beannchar = Still the same^\
Bebbanburg = Bamburgh^\
Benchoer Moer = Ecclesiastical settlement or monastic site at Bangor^\
Beolatun = Bilton^\
Beormaingasham = Birmingham^\
Berewic = Berwick^\
Biedcanford = Luton area^\
Boand = Balbriggan^\
Boher Bue = Boherbue (Bothar Bui)^\
Both Domhnaigh = Bodoney^\
Boweseia = Bawsey^\
Brememium = Newcastle upon Tyne^\
Brycheiniog = Brecon^\
Buais = river Bush^\
Bucgan Ora = Bognor Regis^\
Buireann = Burren^^\
'C'^^\
Caeginesham = Keynsham^\
Caer Baddan = Bath^\
Caer Caradawg = Church Stretton^\
Caer Caratauc = Cary Craddock^\
Caer Daun = Doncaster^\
Caer Didi = Cardiff^\
Caer Durnac = Dorchester^\
Caer Friddyn = Caermarthen^\
Caer Gofannon = Gofannon^\
Caer Guricon = Wroxeter^\
Caer Legeion guar Usic = Caerleon^\
Caer Legeonis = Caerleon upon Uisc, It's actually the same place as above^\
Caer Liwelydd = Carlisle^\
Caer Lloyw = Gloucester^\
Caer Luit Coyt = Wall near Lichfield, obviously slightly misplaced on map; not Lincoln, which is to be identified with Linnuis^\
Caer Magnis = Kenchester^\
Caer Manaw = Isle of Man^\
Caer Maunguid = Manchester^\
Caer-Meguaidd = Meifod^\
Caer Pentaloch = Kirkintilloch^\
Caer Peris = Caer Beris near Builth Wells.^\
Caer Rheon = Cairnryan^\
Caer Riderch = Carrutherstown^\
Caer Segeint = Caernarfon^\
Caer Sws = Caersws^\
Caer Uisc = Exeter^\
Caer Wenddoleu = Carwinley^\
Caer Went = Caerwent^\
Caislen Credi = identified with Scone, where the picts adopted christian belief, therefore 'castle of faith'^\
Camulodunum = Roman city, no longer exists, archaeologists are still not sure of the exact location^\
Camus = Still the same^\
Cantaleah = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Cantmael = Queen Camel^\
Cantwaraburh = Canterbury^\
Cath Atho Dara = Adare^\
Cathair Chonroi = a place near Camp, Ireland^\
Cathures = Glasgow^\
Catraeth = Catterick^\
Ceasterfeld = Chesterfield^\
Ced = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Cetguelli = Kidwelly^\
Cetham = Chatham^\
Chinesburie = Kingsbury^\
Cill Alaid = Killala^\
Cill Chleite = Kilchlief^\
Cill Dara = Killdare^\
Cill Mic Creannain = Kilmacrenan^\
Cindgarath = Kingarth^\
Cinlipiuc = Cynllibiwg^\
Ciorrincg = Charing^\
Cippanhamme = Chipenham^\
Ciren Ceaster = Cirencester^\
Cisse Ceaster = Chichester^\
Clacc Inga Tun = Clacton on Sea^\
Cliath = Could be any village of the region^\
Clogher Mor = Clogher^\
Cluain Meala = Clonmel^\
Cogwy = Old Oswestry 'Maes Cogwy'^\
Colne Ceaster = Colchester^\
Costessey = Still the same^\
Creic = Crayke Castle^\
Creodahanhyll = Credenhill^\
Cruaghan = Cruachan 'Rath Cruachan'; a complex of archaeological sites near Tulsk^\
Cructan = Creechborough Hill^\
Crumbford = Cromford^\
Cuil Conaire = Well known battlefield, Nowadays possibly an insignificant village, greater area with different name,  or no longer exists^\
Cuilenross = Culross^\
Cuince = a mountain in Cualnge^\
Cyddaingastun = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Cymensoraham = Cymenshore^^\
'D'^^\
Daire Calgaigh = Derry (Londonderry)^\
Denetun = Denton^\
Denisesburna = area near Heavenfield^\
Dewyddwella = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Din Baer = possibly Dunbur^\
Din Bych =Tenby^\
Din Draithou = Dunster^\
Din Eydin = Edinburgh^\
Din Erth = possibly Dinerth Castle^\
Din Hua nAmalgada = Castle (Din) of Ui Amalghaid - ancient centre of the kingdom of Amalghaid, today's Barony of Tyrawley^\
Din Reghed = Dunragit^\
Din Tagell = Tintagel^\
Dinas Bran = still the same, a castle near Llangollen, Wales^\
Dinas Emrys = still the same, a fortress near Beddgelert^\
Dinefwr = still the same (sometimes anglicized as Dynevor), a castle near Llandeilo, Wales^\
Dinypas = clearly identified with modern Dunipace, but obviously misplaced on map (Dunipace is to the west of Edinborough)^\
Dofras = Dover^\
Doirad Eilinn = Island of Jura^\
Dol = Dull, near Perth^\
Dol Ais = Dallas, North Scotland^\
Dos Is = Dawlish^\
Dommoc = It is not certainly identified, it's placed within the modern county of Suffolk^\
Dorce Ceaster = Dorceaster^\
Druim Dergblathiug = 'The Red Ridge of Blathuug', pictish battle site, actual place is unknown^\
Drum Ceatt = Possibly an insignificant village, greater area with different name,  or no longer exists, located east of Derry, Ireland^\
Du Glas = Douglas, Lanarkshire^\
Duin Baitte = Dunbeath^\
Duin Bolg = Bolg Fortress, Ireland^\
Duin Caillen = Dunkeld^\
Duin Foither = Dunnottar^\
Duin Ollaigh = Dunolly^\
Dumanyn = Dalmeny, as it is called today, lies near Dunipace^\
Dumha Aichir = Possibly an insignificant village, greater area with different name,  or no longer exists, well-known battlefield, located in Leinster^\
Dun Aberte = Dunaverty^\
Dun At = Dunadd^\
Dun Breattann = Dumbarton^\
Dun Buicead = Dunboyke^\
Dun Cethern = Giant's Sconce^\
Dun Chuile = Headford^\
Dun Cuair = Located in Enfield^\
Dun Daig = Dundee^\
Dun Devenel = Dundonald^\
Dun Duirn = located in Perthshire^\
Dun Iasgach = Munster^\
Dun Keltair = Downpatrick^\
Dun Nechtain = Dunnichen OR Dunachton scholars are still uncertain^\
Dun Sebuirge = Dunseverick^\
Dun Taruo = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Dun gCrot = fort at foot of Sliabh Grud^\
Dun na mBarc = Bantry Bay in Cork^\
Dwfr = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Dyvnwtdd = Possibly an insignificant village, greater area with different name,  or no longer exists^^\
'E'^^\
Earnningtun = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Eclesia Hyll = Eccleshill^\
Eglesfeld = Still the same^\
Egleshalh = Eccleshall^\
Eglwys Tysilio = Meiford^\
Ego = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Eifionydd = Still the same^\
Eldretune = Aldrington^\
Elfed = Possibly refers to Cynwyl Elfed^\
Elmwella = Elmswell^\
Emain Macha = Navan Fort^\
Eoferwic = York^\
Erging = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Essovre = Ashover^\
Esterteferd = Bishop's Stortford^\
Ewias = 'Ewyas' early Welsh kingdom which may have been formed around the time of the Roman withdrawal from Britain in the 5th century, the village is named after the valley.^^\
'F'^^\
Faffand = a place in County Offaly, mentioned in Ancient chronicles^\
Fearr Leah = Possibly an insignificant village, greater area with different name,  or no longer exists^^\
'G'^^\
Genouhalh = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Gyppeswic = Ipswich^\
Gislheresuuyrth = Isleworth^\
Glouvia = Gloucester^\
Gobhan = Brigown^\
Grafrenn = ancient site north of Dunboyne^\
Grantebrycge = Cambridge^\
Grwst = Possibly an insignificant village, greater area with different name,  or no longer exists affiliated with St. Grwst^\
Gyldeford = Guildford^^\
'H'^^\
Halhfeax = Halifax^\
Hamtun = Still the same^\
Hanstige = Anstey^\
Hefenfelth = Heavenfield^\
Helfeld = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Herr Hlaw = The exact location is unknown, the name is composed by Herr (army) and hlaw (hill or burial mound), thus 'The Hill of the dead Soldiers'^\
Hlew Ceaster = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Hreopedun = Repton^\
Hrofaes Ceaster = Rochester^\
Huensis = Insula Huensis - Iona on Mull (on the map some water is missing depriving Mull of its island status)^\
Hyncaleah = Hinckley, Leicestershire^\
Hyrne Ceaster = Horncastle^\
Hysetun = Histon^^\
'I'^^\
Ilea = Isle of Islay^\
Imchlar = area near Donaghmore^\
Inderawuda = Beverley^\
Ir Ysgyn = Erskine^\
Irrus Domnann = the barony of Erris, in County Mayo^\
Isura = Possibly an insignificant village, greater area with different name,  or no longer exists^^\
'L'^^\
Lann Abae = Possibly Lundaff^\
Leim an Eich = Droichead^\
Leodridan = Leatherhead^\
Licidfelth = Lichfield^\
Ligor Ceaster = Leicester^\
Linnuis = Lindsey^\
Llan = Still the same^\
Llan Forfael = Lanfaire^\
Llan Heledd = Llanhilleth^\
Llan y Hadein = Llanhuadain^\
Llanerch = Llanerchymedd^\
LlangWern = Still the same OR Llanwern^\
Llangollen = Still the same^\
Llanidloes = Still the same^\
Llyn = The Llŷn Peninsula^\
Llys Pengwern = Possibly Whittington^\
Loidis = Leeds^\
Lois Mor = Lismore^\
Luachair = Caochan Luachair^\
Lugmud = Louth^\
Luimneach Laighean = area of Wexford^\
Luith Feirn = historically recorded battle site, location is actually unknown^\
Lundenwic = London^\
Lyme = Newcastle under Lyme^^\
'M'^^\
Maes Cogwy = Maserfield^\
Maesmor = The same^\
Mag Liphi = Liffey^\
Mag Mucceda = an area near Navan Fort^\
Mag Tuired = in modern Irish Magh Tuireadh OR anglicised as Moytura or Moytirra; a battlefield^\
Mag uillin = Moycullen^\
Mageduac = Mugdock^\
Magh Gals = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Magh Rath = Well known battlefield^\
Mercheham = Marcham^\
Merarrian Cynog = Still the same^\
Merarrian Tydfil = Still the same^\
Middelsburh = Middlesburgh^\
Moel Fryn = Malvern Hills^\
Monidhcrobh = Moncreiffe Hill^\
Morbeth = Morpeth^\
Mynyw = St. Davids^^\
'N'^^\
Nisa = Inverness, perhaps slightly misplaced on map^\
Niwantune = Newton^\
Norwic = Norwich^^\
'O'^^\
Opergelei = Apergele^\
Oratun = likely to be Chipping Norton or Hook Norton, Norton being a corruption of Oratun^\
Oxenaforda = Oxford^^\
'P'^^\
Pabell = Possibly near Machynlleth^\
Pairc Mor = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Pen Rhionydd = located in Peniarth^\
Pencaer = Still the same^\
Pillgwynllwg = Gwynllwg - Wentlooge^\
Poclintun = Pocklington^\
Portesmuda = Portsmouth^\
Pulais = Possibly an insignificant village, greater area with different name,  or no longer exists^^\
'R'^^\
Rae Ban = actually mythological site of the Cu Chulainn Saga^\
Raith Bec = Rathbeg^\
Rath Clochair = ancient centre of the barony of Rosclogher^\
Rath Cormac = Rathcormac^\
Rath Luraig = Maghera^\
Rendlaesham = Still the same^\
Rhaeadr Gwy = Rhayader^\
Rhyd Ruth = Redruth^\
Ricestun = perhaps Cyricestun, a place mentioned in Chronicles, relating to Aelfred of Wessex^\
Ruim = Still the same^^\
'S'^^\
Scythles = seems to be North or South Shields^\
Seals ey = Selsey^\
Searoburh = Old Sarum^\
Sleamhain = Sleamaine, a hill in Co. Wicklow^\
Sliab Culinn = Hollymount^\
Snetesham = Snettisham^\
Swanawic = Swanage^^\
'T'^^\
Taceham = Thatcham^\
Taddanleage = Tadley^\
Tairpert Boitir = Tarbert^\
Tamaris = ancient Cornish settlement on the River Tamar, mentioned in the 7th century 'Ravenna Cosmology'^\
Tappingtun = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Tatessete = Tattersette^\
Temair = Area of Dublin^\
Theodford = Thetford^\
Tuidhidhean = Tynan^^\
'U'^^\
Uaine = Area in Scotland^\
Urnaidhe = Urney^^\
'V'^^\
Vernalis = ancient Cornish settlement east of Exeter (=Caer Uisc), mentioned in the same Chronicle as Tamaris^\
Vintan Ceaster = Winchester^^\
'W'^^\
Waldham = Waltham^\
Weargebuman = South Warnborough^\
Wellatun = Welton^\
Weorthingtun = Worthington^\
Westarham = Westerham^\
Wicstun = Market Weighton^\
Winteringasham = Winteringham^\
Wlencing = Lancing^\
Wudetun = Wootton Bassett^^\
'Y'^^\
Ynas Towy = Possibly an insignificant village, greater area with different name,  or no longer exists^\
Ynys Manaw = Isle of Man^\
Ynys Metcaut = Lindisfarne^\
Ynys Mon = The Isle of Anglesey^\
Yr Wyn = Irvine, Ayreshire."),

 ("diccionario_brytenwalda", "The Brytenwalda Dictionary",
  "The Great Ancient Languages Dictionary by Adorno.^^\
'A'^^\
Aberystwyth = Aberystwyth^\
Ad Gefrin = Yeavering^\
Aillt = Villager^\
Alne Ceaster = Alcester^\
Arras = Free men or nobles^\
'B'^^\
Beadu rinc = battle man^\
Bebbanburh = Bamburgh^\
Beormaingasham = Birmingham^\
Bernaccia = The most part of modern day Northumbria^\
Bonheddwr = Gentleman^\
Brenin = King^\
'C'^^\
Caer Daun = Dorchester^\
Caer Didi = Cardiff^\
Caer Durnac = Dorchester^\
Cait = Caithness - Cait was the most powerful Pictish kingdom in the VII century, subjecting others (Pictland)^\
Cantwaraburh = Canterbury^\
Cantware = Kent^\
Ceither(ne) = A band or troops of levied soldiers. Anglicised to Kern^\
Colne Ceaster = Colchester^\
Cyning = king^\
'D'^^\
Dena = Danish^\
Dinas Eidyn = Edinburgh^\
Din Tagell = Tintagel^\
Dofras = Dover^\
Dryhten = Warlord, master^\
Duguth = manly, honourable person, veteran^\
Dun At = Dunadd^\
'E'^^\
Ealdorman = elder man = senator, member of the royal council^\
East Engla = East Anglia^\
East Seaxna = Essex^\
Engle = Angle^\
Eoferwic = York^\
'F'^^\
Fresena = Frisian^\
'G'^^\
Gaisgidh - Warrior (this is old Irish, the modern form is gaiscioch)^\
Gebur = Farmer, Dweller^\
Geneat = Companion, high ranking Ceorl. Meaning: One who enjoys (certain priviliges)^\
Geoguth = Young man or untested warrior^\
Gesith = Companion, Follower^\
Gippeswic = Ipswich^\
Gosgordd = Escort, guard^\
Grantebrycge = Cambridge^\
Gwrda = Companion ^^\
'H'^^\
Hearthweru = hearth - weru, someone who has the right to sit at the same fire (=hearth) as the noble family^\
'K'^^\
Kotsetla = cot-setla = cottage settler, a free man who owns his own house^\
'L'^^\
Lindisware = Lindisfarne^\
Loidis = Leeds^\
Lundenwic = London^\
'M'^^\
Marcach - Horseman^\
Mierce (The March) = Mercia^\
'O'^^\
Oxenaforda = Oxford^\
Ocaire = Another rank of farmer, one who owned seven of each of the major animals - cows, sheep and pigs.^\
'P'^^\
Pedit = Footman ^\
Portesmuda = Portsmouth^\
'R'^^\
Hrofaes Ceaster = Rochester^\
Ri = King (Ard Ri = High King)^\
'S'^^\
Saethydd = Archer ^\
Salinae = Salt (mine)^\
Sceotand = Shooting, firing missiles^\
Scoti = Irish raiders^\
Seaxe = Saxon^\
Seaxna = Saxons^\
Suth Seaxna = Sussex^^\
'T'^^\
Taoiseach - Chieftain^\
Teulu = Family ^\
Theow = Slave, unfree man^\
Tiarna = Lord (Ard Tiarna = High Lord)^\
Tywysog = Prince^\
'U'^^\
Uchelwr = Nobleman^\
Udd = Lord^^\
'V'^^\
Varchogyon = horseman/knight^\
Vintan Ceaster = Winchester^^\
'W'^^\
Wylisc = Welsh^^\
Interesting link to an Anglo-Saxon dictionary: http://www.utexas.edu/cola/centers/lrc/books/asd/dict-L.html^^\
English place names: http://www.englishplacenames.co.uk/"),
 ("formations", "Formations", 
"The formations mod is an extensive reworking of the original simple interface by Mirathei. At a command, infantry can form in ranks by level, ranks by shield/weapon, wedge by level, or square. Cavalry can form a wedge. Formations follow all battlefield commands, including from the battle panel. Native AI is given the ability to make the same formations.^^\
For Hold and Follow commands, default division placement around the player is: infantry to the left, cavalry to the right, and archers up front. Additional infantry divisions set up further left, additional cavalry further right, and additional ranged further forward. So, for example, if you would like TWO ranged divisions and want the one with thrown weapons further forward, make sure the archers are in Division 3 and the skirmishers in a Division 4-9.^^\
Troop divisions that for whatever reason are NOT in formation will attempt to integrate with the other divisions in the \"Hold\" position. These divisions will maintain the same FACING that the player had unless the player checks the autorotate option in the Formations Options Menu under the Preferences Menu under the Camp Menu.^^\
The player may override default placement through the additional F2 Menu command to memorize division(s) position relative to the player. So if you prefer, for example, your cavalry in front and your archers behind, rearrange these divisions during a quiet battle and then press F2-F7. Just make sure to stand toward the rear when memorizing and pad your new arrangement with plenty of space, as changes in division sizes, position rotations, and map borders affect the precision of memorized placement.^^\
Player troops start every battle in Hold position around the player, utilizing either default or memorized placement and formation.^^\
Placement is overridden for any division the player chooses to personally head through the Formations Options menu.^^\
There are no assumptions about division type beyond the first THREE. The system types them as the following:^^\
    - majority HEROES: majority skilled, Support; otherwise Bodyguard^^\
    - majority HORSES: majority with bows, Mounted Archers; otherwise regular Cavalry^^\
    - majority RANGED: with thrown weapon, Skirmishers; otherwise regular Ranged^^\
    - none of the above: majority with polearms, Polearms; otherwise regular Infantry^^\
You have to bear this typing scheme in mind when composing divisions; otherwise an additional Infantry division may suddenly become some sort of Ranged when you add, say, recruits with slings. Also be aware that Brytenwalda autoequips troops with ranged weapons at the start of battle, thereby changing their type for divisions beyond the first three.^^\
Hero-type divisions and more notably Skirmishers make infantry-type formations. Skirmishers will revert to type Infantry (and change default placement on \"Hold\" to the players LEFT instead of FORWARD) when they use up their ammunition.^^\
Whenever a unit first forms a particular formation, troops spread out for ease of forming up. They also change weapons as befitting their new positions within their formation. The mod also strips swing capability from stabbing weapons for infantry in formation, the better to use in close quarters. You may wish to experiment with formation spacing to see which works best for its majority weapon. Troops with long axes, for example, benefit from a couple extra spaces to swing in.^^\
The \"ranks\" command for archers puts them in a staggered line.^^\
Cavalry will not make any formation other than the wedge.^^\
Charge (and Dismount for cavalry) will undo a formation. The player may Advance multiple times to have a formation move toward the average position of the enemy. Or use the order panel or Hold-F1 to place them (or sweep them across the enemy in the case of the cavalry wedge).^^\
Speaking of which, the Hold-F1 command has been expanded: when done on an enemy formation, player divisions will attack it. Infantry formations will advance into melee without breaking formation, cavalry will revert into a Native style charge after closing, and archers will advance until they start shooting. In any case, if the target is wiped out, the player division will return to the player."),
     ("credits", "Brytenwalda team credits", "^Main Team^^\
^Idibil \
^Adorno\
^Motomataru\
^BrustwarzenLenny\
^Life_Erikson\
^Obi Juan Kenobi\
^Morcant\
^Gwalchawad\
^Thandrius\
^Rathmor\
^Phaiak\
^Vaelicus^^\
^Others and more information: http://forums.taleworlds.com/index.php/topic,135589.msg3683420.html"), 
]
