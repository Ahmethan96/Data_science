import {Configuration, OpenAIApi} from "openai";

const configuration = new Configuration({
    organization: "#####",
    apiKey: "#####"
})

const openai = new OpenAIApi(Configuration);

const completion = await openai.createChatCompletion({
    model: "gpt-3.5-turbu",
    messages: [
        {role: "user", content: "Hello World"}
    ]
})

console.log(completion.data.choices[0].messages);
