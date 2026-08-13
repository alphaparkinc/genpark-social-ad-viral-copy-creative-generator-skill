class SocialAdViralCopyCreativeGeneratorClient:
    def generate_ad_creatives(self, target_product: str, platform: str = "TikTok") -> dict:
        copies = [
            "Stop doing this manually in 2026! Here is the AI workflow you need.",
            "This 1 simple AI tool saved our team 20 hours a week."
        ]
        hooks = ["Text overlay: 'Don't scroll before seeing this'", "Fast-cut demo transition"]
        return {
            "ad_copy_variants": copies,
            "visual_hooks": hooks,
            "predicted_ctr_score": 4.85
        }
