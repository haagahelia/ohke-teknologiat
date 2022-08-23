# Main steps of paranoidly safe Linux installation

0. Take into safety all old files, photos, links, maybe even useful command history you want to keep!
1. Download the Linux distribution image via some **safe network**, like cellular network (possibly VPN secured too)
1. Wipe the old discs, possibly once with shred command, and install the Linux distro **without connecting** to network
1. *sudo ufw enable*         // **enabling firewall rules**
1. Using still the cellular network or other **safe network**, run the updates: *sudo apt update*
1. Only now connect to **normal network** (You have got the authentic distro image, real updates and the firewall is setup) 