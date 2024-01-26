if ! top -bn1 | grep frpc > /dev/null; then
    echo "frpc is not running, start frpc"
    tmux new -d -s std_remote
    tmux send -t std_remote 'cd /home/tmp/code/pc/frp/frp_0.33.0_linux_amd64' Enter
    tmux send -t std_remote './frpc -c frpc.ini' Enter
else
    echo "frpc is running"
fi
