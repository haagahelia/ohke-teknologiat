import { Kafka, logLevel } from 'kafkajs'; 
console.log("*** Admin starts... (Only needed once for each created Kafka server, actually) ***");

const kafka = new Kafka({
    clientId: 'my-admin-create-app',
    brokers: ['localhost:9092'],
    logLevel: logLevel.INFO
});

const admin = kafka.admin();

const run = async () => {

    await admin.connect();

    const topics = await admin.listTopics();

    if(!topics.includes("tobechecked")) {
        await admin.createTopics({
            validateOnly: false,
            waitForLeaders: true,
            timeout: 5000,
            topics: [
                {
                    topic: "tobechecked",
                    numPartitions: 1,     // default: -1 (uses broker `num.partitions` configuration)
                    replicationFactor: 1, // default: -1 (uses broker `default.replication.factor` configuration)
                    replicaAssignment: [],  // Example: [{ partition: 0, replicas: [0,1,2] }] - default: []
                    configEntries: []       // Example: [{ name: 'cleanup.policy', value: 'compact' }] - default: []
                },
            ]
        });
    } else {
        console.log("Topics already created!");
    }
    await admin.disconnect()
    console.log("*** Admin create topic steps completed ***");
};

run().catch(console.error);