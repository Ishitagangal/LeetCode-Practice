public class TokenBucket{
    private final long maxBucketSize;
    private final long refillRate; // per minute?

    private double currentBucketSize;
    private long lastRefillTimestamp;

    public TokenBucket(long maxBucketSize, long refillRate){
        this.maxBucketSize = maxBucketSize;
        this.refillRate = refillRate;
        this.currentBucketSize = maxBucketSize;
        this.lastRefillTimestamp = System.nanoTime();
    }

    public synchronized boolean allowRequest(int tokens){
        refill();
        if(this.currentBucketSize > tokens){
            currentBucketSize -= tokens;
            return true;
        }
        return false;
    }

    private void refill(){
        long now = System.nanoTime();
        double tokensToAdd = (now - this.lastRefillTimestamp) * this.refillRate /1e9;
        this.currentBucketSize = Math.min(maxBucketSize, currentBucketSize + tokensToAdd);
        lastRefillTimestamp = now;
    }

}