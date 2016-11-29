outnet_exec python getURList.py > urlist.log
awk -F['\t'] '{if(NF==2) print $0}' urlist.log > urlist.txt
python crawl_comment.py urlist.txt
