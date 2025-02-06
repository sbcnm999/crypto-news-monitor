import flet as ft
from datetime import datetime
import requests
from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class CryptoMention:
    crypto_name: str
    symbol: str
    count: int

@dataclass
class ContractAddress:
    address: str
    blockchain: str

@dataclass
class Tweet:
    id: str
    tweet_id: str
    author: str
    content: str
    created_at: datetime
    sentiment_score: float
    crypto_mentions: List[CryptoMention] = None
    contract_addresses: List[ContractAddress] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'Tweet':
        crypto_mentions = []
        if data.get('crypto_mentions'):
            crypto_mentions = [
                CryptoMention(
                    crypto_name=mention['crypto_name'],
                    symbol=mention['symbol'],
                    count=mention['count']
                )
                for mention in data['crypto_mentions']
            ]

        contract_addresses = []
        if data.get('contract_addresses'):
            contract_addresses = [
                ContractAddress(
                    address=addr['address'],
                    blockchain=addr['blockchain']
                )
                for addr in data['contract_addresses']
            ]

        return cls(
            id=data['id'],
            tweet_id=data['tweet_id'],
            author=data['author'],
            content=data['content'],
            created_at=datetime.fromisoformat(data['created_at']),
            sentiment_score=float(data['sentiment_score']),
            crypto_mentions=crypto_mentions,
            contract_addresses=contract_addresses,
        )

class ApiClient:
    def __init__(self, base_url: str = 'http://localhost:8000/api/v1'):
        self.base_url = base_url

    def get_tweets(self, skip: int = 0, limit: int = 20) -> List[Tweet]:
        try:
            response = requests.get(
                f'{self.base_url}/tweets/',
                params={'skip': skip, 'limit': limit}
            )
            response.raise_for_status()
            return [Tweet.from_dict(tweet) for tweet in response.json()]
        except Exception as e:
            print(f"Error fetching tweets: {e}")
            return []

    def get_crypto_mentions_summary(self) -> Dict[str, Any]:
        try:
            response = requests.get(f'{self.base_url}/crypto_mentions/summary')
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching crypto mentions summary: {e}")
            return {}

    def get_economic_indicators_summary(self) -> Dict[str, Any]:
        try:
            response = requests.get(f'{self.base_url}/economic_indicators/summary')
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching economic indicators summary: {e}")
            return {}

class TweetCard(ft.Card):
    def __init__(self, tweet):
        super().__init__()
        self.tweet = tweet
        
        # Create tweet content
        content = ft.Column(
            controls=[
                # Header info
                ft.Row(
                    controls=[
                        ft.Text(f"@{tweet.author}", size=16, weight=ft.FontWeight.BOLD),
                        ft.Text(self.format_time(tweet.created_at), color=ft.colors.GREY_500),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                # Tweet content
                ft.Text(tweet.content, size=14, selectable=True),
                # Sentiment score
                ft.Text(
                    f"Sentiment: {tweet.sentiment_score:.2f}",
                    color=ft.colors.GREEN if tweet.sentiment_score > 0 else ft.colors.RED,
                ),
            ],
            spacing=10,
        )
        
        # Crypto mentions
        if tweet.crypto_mentions:
            crypto_row = ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(mention.crypto_name),
                        bgcolor=ft.colors.BLUE_GREY_100,
                        border_radius=5,
                        padding=5,
                    )
                    for mention in tweet.crypto_mentions
                ],
                wrap=True,
                spacing=5,
            )
            content.controls.append(crypto_row)
        
        # Contract addresses
        if tweet.contract_addresses:
            for addr in tweet.contract_addresses:
                addr_row = ft.Row(
                    controls=[
                        ft.Text(f"{addr.address[:10]}..."),
                        ft.IconButton(
                            icon=ft.icons.COPY,
                            tooltip="Copy address",
                            on_click=lambda e, a=addr.address: self.copy_address(e, a),
                        ),
                    ]
                )
                content.controls.append(addr_row)
        
        self.content = ft.Container(
            content=content,
            padding=10,
        )
    
    def format_time(self, dt):
        now = datetime.now()
        diff = now - dt
        if diff.days > 0:
            return f"{diff.days}d ago"
        hours = diff.seconds // 3600
        if hours > 0:
            return f"{hours}h ago"
        minutes = diff.seconds // 60
        return f"{minutes}m ago"
    
    def copy_address(self, e, address):
        e.page.set_clipboard(address)
        e.page.show_snack_bar(ft.SnackBar(content=ft.Text("Address copied to clipboard")))

class CryptoNewsApp:
    def __init__(self):
        self.api_client = ApiClient()
        self.current_page = 0
        self.tweets = []
    
    def main(self, page: ft.Page):
        page.title = "Crypto News Monitor"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        
        # Create tabs view
        self.tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="Tweets",
                    content=ft.Column(scroll=ft.ScrollMode.AUTO),
                ),
                ft.Tab(
                    text="Stats",
                    content=ft.Column(scroll=ft.ScrollMode.AUTO),
                ),
            ],
            expand=1,
        )
        
        # Create refresh button
        refresh_btn = ft.FloatingActionButton(
            icon=ft.icons.REFRESH,
            on_click=self.refresh_data,
        )
        
        # Create load more button
        self.load_more_btn = ft.ElevatedButton(
            text="Load More",
            on_click=self.load_more_tweets,
        )
        
        # Main layout
        page.add(
            self.tabs,
            ft.Container(
                content=refresh_btn,
                alignment=ft.alignment.bottom_right,
                padding=20,
            ),
        )
        
        # Load initial data
        self.load_tweets(page)
        self.update_stats(page)
        
        # Set up auto-refresh
        page.on_interval(60000, lambda _: self.refresh_data(None))
    
    def load_tweets(self, page):
        tweets = self.api_client.get_tweets(skip=self.current_page * 20)
        tweets_column = self.tabs.tabs[0].content
        
        for tweet in tweets:
            tweets_column.controls.append(TweetCard(tweet))
        
        if not self.load_more_btn in tweets_column.controls:
            tweets_column.controls.append(self.load_more_btn)
        
        self.tweets.extend(tweets)
        page.update()
    
    def load_more_tweets(self, e):
        self.current_page += 1
        self.load_tweets(e.page)
    
    def refresh_data(self, e):
        page = e.page if e else self.tabs.page
        
        # Clear existing tweets
        tweets_column = self.tabs.tabs[0].content
        tweets_column.controls.clear()
        self.tweets = []
        self.current_page = 0
        
        # Reload data
        self.load_tweets(page)
        self.update_stats(page)
    
    def update_stats(self, page):
        stats_column = self.tabs.tabs[1].content
        stats_column.controls.clear()
        
        # Crypto stats
        crypto_stats = self.api_client.get_crypto_mentions_summary()
        if crypto_stats:
            stats_column.controls.append(
                ft.Text("Cryptocurrency Mentions", size=20, weight=ft.FontWeight.BOLD)
            )
            for crypto, count in crypto_stats.items():
                stats_column.controls.append(
                    ft.Text(f"{crypto}: {count} mentions")
                )
        
        # Economic indicators stats
        economic_stats = self.api_client.get_economic_indicators_summary()
        if economic_stats:
            stats_column.controls.append(
                ft.Text("Economic Indicators", size=20, weight=ft.FontWeight.BOLD)
            )
            for indicator, value in economic_stats.items():
                stats_column.controls.append(
                    ft.Text(f"{indicator}: {value}")
                )
        
        page.update()

def main(page: ft.Page):
    app = CryptoNewsApp()
    app.main(page)

ft.app(target=main, view=ft.AppView.FLET_APP)
