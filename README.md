# 陣取りゲーム

https://github.com/kaga1minn0nnn4/TurfWarServer/assets/35623953/b8d6f6f1-9876-4c44-97cc-cd1b8df5e7ca

## なにこれ
コンピュータネットワークの課題で制作した2D版スプラトゥーンみたいなゲームです。

## 起動方法
    git clone https://github.com/kaga1minn0nnn4/TurfWarServer.git
    cd TurfWarServer

    # サーバー起動
    python3 main.py

    # サーバー起動(IPとポート指定)
    python3 main.py --server_ip 192.168.0.1 --server_port 8000

    # クライアント起動
    python3 client.py

    # NPCクライアント起動
    python3 client.py --mode npc

    # クライアント起動(サーバーIPとポート指定)
    python3 client.py --server_ip 192.168.0.1 --server_port 8000

## ルール
プレイヤーはランダムで生成されたマップ内を動き回りながら、マップ内を塗りつぶして行きます。\
最終的により多くの陣地を塗ったプレイヤーの勝利となります。

## 操作方法
### 移動について
w, a, s, dでマップ内の空白の部分を移動できます。\
*の部分は通行不可です。

### アイテムについて
- マップ内の?マークを踏むとアイテムが手に入ります。
- アイテムを踏んだ次のターンからアイテムを使用するか聞かれるので、1を入力するとアイテムを使用します。
- アイテムの効果はランダムで、アイテムを取得したときに決定します。マリカみたいな感じです。
- アイテムは1個まで保持できて、アイテムを持った状態で?マークを踏むと上書きされます。

## バグとか改善点とか
- 片方のプレイヤーが切断したときにもう片方のプレイヤーにうまく通知されないので変なことになる。
