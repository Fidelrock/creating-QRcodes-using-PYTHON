# the dark module in darkblue color

import segno
qrcode = segno.make_qr("https://github.com/Fidelrock")

qrcode.save("githubPortfolio.png",
            scale=5,
            border=10,
            dark = "darkblue",
            quiet_zone = "lightgrey",
            )

