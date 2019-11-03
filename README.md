# mattbot

Files
<table border="1" class="docutils">
<colgroup>
<col width="36%">
<col width="64%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">__init__.py</span></code></td>
<td>an empty file that helps python find your actions</td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">actions.py</span></code></td>
<td>code for your custom actions</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">config.yml</span></code> ‘*’</td>
<td>configuration of your NLU and Core models</td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">credentials.yml</span></code></td>
<td>details for connecting to other services</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">data/nlu.md</span></code> ‘*’</td>
<td>your NLU training data</td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">data/stories.md</span></code> ‘*’</td>
<td>your stories</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">domain.yml</span></code> ‘*’</td>
<td>your assistant’s domain</td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">endpoints.yml</span></code></td>
<td>details for connecting to channels like fb messenger</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">models/&lt;timestamp&gt;.tar.gz</span></code></td>
<td>my initial model</td>
</tr>
</tbody>
</table>

1. nlu.md
NLU stands for Natural Language Understanding, which means turning user messages into structured data. To do this with Rasa, you provide training examples that show how Rasa should understand user messages, and then train a model by showing it those examples.
Intents are groups of messages with the same meaning. Rasa’s job will be to predict the correct intent when your users send new, unseen messages to your assistant. 

2. config.yml
Make NLU model use the supervised_embeddings pipeline

3. stories.md
Dialogue management (how to respond to your messages)
Core models learn from real conversational data in the form of training “stories”. A story is a real conversation between a user and an assistant. Lines with intents and entities reflect the user’s input and action names show what the assistant should do in response.
Lines that start with - are actions taken by the assistant

4. domain.yml
The universe our bot lives in: what user inputs it should expect to get, what actions it should be able to predict, how to respond, and what information to store.
<table border="1" class="docutils">
<colgroup>
<col width="20%">
<col width="80%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">intents</span></code></td>
<td>things you expect users to say</td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">actions</span></code></td>
<td>things mattbot can do and say</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">templates</span></code></td>
<td>template strings for the things mattbot can say</td>
</tr>
</tbody>
</table>

5. train
rasa train
