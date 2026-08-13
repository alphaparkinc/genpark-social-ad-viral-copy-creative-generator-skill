from client import SocialAdViralCopyCreativeGeneratorClient

def main():
    client = SocialAdViralCopyCreativeGeneratorClient()
    res = client.generate_ad_creatives("AI Smart Watch", "Instagram Reels")
    print(f"Predicted CTR Score: {res['predicted_ctr_score']}%")
    print("Ad Copy Variants:", res["ad_copy_variants"])

if __name__ == "__main__":
    main()
