%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-l
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1351:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyph-utf8.tar.xz
Source1352:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyph-utf8.doc.tar.xz
Source1354:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-base.tar.xz
Source1355:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifluatex.tar.xz
Source1356:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifluatex.doc.tar.xz
Source1358:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifxetex.tar.xz
Source1359:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifxetex.doc.tar.xz
Source1400:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyperref.tar.xz
Source1401:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyperref.doc.tar.xz
Source1467:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ijqc.tar.xz
Source1468:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ijqc.doc.tar.xz
Source1469:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/inlinebib.tar.xz
Source1470:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/inlinebib.doc.tar.xz
Source1471:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iopart-num.tar.xz
Source1472:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iopart-num.doc.tar.xz
Source1571:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphenex.tar.xz
Source1905:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifsym.tar.xz
Source1906:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifsym.doc.tar.xz
Source1907:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/inconsolata.tar.xz
Source1908:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/inconsolata.doc.tar.xz
Source1909:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/initials.tar.xz
Source1910:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/initials.doc.tar.xz
Source1911:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ipaex-type1.tar.xz
Source1912:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ipaex-type1.doc.tar.xz
Source2289:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifetex.tar.xz
Source2290:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifetex.doc.tar.xz
Source2292:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iftex.tar.xz
Source2293:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iftex.doc.tar.xz
Source2294:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/insbox.tar.xz
Source2295:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/insbox.doc.tar.xz
Source2492:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-ethiopic.tar.xz
Source2497:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-arabic.tar.xz
Source2498:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-farsi.tar.xz
Source2499:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/imsproc.tar.xz
Source2500:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/imsproc.doc.tar.xz
Source2520:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-chinese.tar.xz
Source2521:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/impatient-cn.doc.tar.xz
Source2553:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-bulgarian.tar.xz
Source2554:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-mongolian.tar.xz
Source2555:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-russian.tar.xz
Source2558:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-serbian.tar.xz
Source2559:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-ukrainian.tar.xz
Source2600:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-czech.tar.xz
Source2601:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-slovak.tar.xz
Source2607:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-english.tar.xz
Source2619:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/impatient.doc.tar.xz
Source2620:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/intro-scientific.doc.tar.xz
Source2670:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-armenian.tar.xz
Source2671:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-croatian.tar.xz
Source2672:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-danish.tar.xz
Source2673:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-dutch.tar.xz
Source2674:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-estonian.tar.xz
Source2675:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-finnish.tar.xz
Source2676:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-friulan.tar.xz
Source2677:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-hungarian.tar.xz
Source2678:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-hungarian.doc.tar.xz
Source2679:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-icelandic.tar.xz
Source2680:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-irish.tar.xz
Source2681:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-kurmanji.tar.xz
Source2682:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-latin.tar.xz
Source2683:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-latvian.tar.xz
Source2684:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-lithuanian.tar.xz
Source2685:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-norwegian.tar.xz
Source2686:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-piedmontese.tar.xz
Source2687:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-romanian.tar.xz
Source2688:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-romansh.tar.xz
Source2689:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-slovenian.tar.xz
Source2690:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-swedish.tar.xz
Source2691:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-turkish.tar.xz
Source2692:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-uppersorbian.tar.xz
Source2693:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-welsh.tar.xz
Source2718:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-basque.tar.xz
Source2719:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-french.tar.xz
Source2720:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/impatient-fr.doc.tar.xz
Source2721:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/impnattypo.tar.xz
Source2722:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/impnattypo.doc.tar.xz
Source2763:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-german.tar.xz
Source2810:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-greek.tar.xz
Source2811:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-greek.doc.tar.xz
Source2812:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-ancientgreek.tar.xz
Source2813:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ibycus-babel.tar.xz
Source2814:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ibycus-babel.doc.tar.xz
Source2816:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ibygrk.tar.xz
Source2817:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ibygrk.doc.tar.xz
Source2837:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-indic.tar.xz
Source2838:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-sanskrit.tar.xz
Source2860:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-italian.tar.xz
Source2874:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ipaex.tar.xz
Source2875:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ipaex.doc.tar.xz
Source2935:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-afrikaans.tar.xz
Source2936:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-coptic.tar.xz
Source2937:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-esperanto.tar.xz
Source2938:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-georgian.tar.xz
Source2939:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-indonesian.tar.xz
Source2940:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-interlingua.tar.xz
Source2941:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-thai.tar.xz
Source2942:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-turkmen.tar.xz
Source2952:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-polish.tar.xz
Source2978:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-portuguese.tar.xz
Source2986:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-catalan.tar.xz
Source2987:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-galician.tar.xz
Source2988:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-spanish.tar.xz
Source3035:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/index.tar.xz
Source3036:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/index.doc.tar.xz
Source3372:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifmtarg.tar.xz
Source3373:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifmtarg.doc.tar.xz
Source4268:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hypdvips.tar.xz
Source4269:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hypdvips.doc.tar.xz
Source4270:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyper.tar.xz
Source4271:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyper.doc.tar.xz
Source4273:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hypernat.tar.xz
Source4274:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hypernat.doc.tar.xz
Source4276:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyperxmp.tar.xz
Source4277:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyperxmp.doc.tar.xz
Source4279:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphenat.tar.xz
Source4280:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphenat.doc.tar.xz
Source4282:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/idxcmds.tar.xz
Source4283:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/idxcmds.doc.tar.xz
Source4284:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/idxlayout.tar.xz
Source4285:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/idxlayout.doc.tar.xz
Source4287:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifmslide.tar.xz
Source4288:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifmslide.doc.tar.xz
Source4289:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifnextok.tar.xz
Source4290:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifnextok.doc.tar.xz
Source4292:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifoddpage.tar.xz
Source4293:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifoddpage.doc.tar.xz
Source4295:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifplatform.tar.xz
Source4296:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifplatform.doc.tar.xz
Source4298:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifthenx.tar.xz
Source4299:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifthenx.doc.tar.xz
Source4300:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iitem.tar.xz
Source4301:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iitem.doc.tar.xz
Source4303:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/image-gallery.tar.xz
Source4304:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/image-gallery.doc.tar.xz
Source4305:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/imakeidx.tar.xz
Source4306:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/imakeidx.doc.tar.xz
Source4308:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/import.tar.xz
Source4309:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/import.doc.tar.xz
Source4310:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/incgraph.tar.xz
Source4311:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/incgraph.doc.tar.xz
Source4312:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/indextools.tar.xz
Source4313:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/indextools.doc.tar.xz
Source4315:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/inlinedef.tar.xz
Source4316:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/inlinedef.doc.tar.xz
Source4318:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/inputtrc.tar.xz
Source4319:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/inputtrc.doc.tar.xz
Source4321:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/interactiveworkbook.tar.xz
Source4322:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/interactiveworkbook.doc.tar.xz
Source4323:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/interfaces.tar.xz
Source4324:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/interfaces.doc.tar.xz
Source4326:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/inversepath.tar.xz
Source4327:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/inversepath.doc.tar.xz
Source4329:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/invoice.tar.xz
Source4330:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/invoice.doc.tar.xz
Source5757:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/interpreter.tar.xz
Source5758:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/interpreter.doc.tar.xz
Source5850:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/interval.tar.xz
Source5851:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/interval.doc.tar.xz
Source5852:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ionumbers.tar.xz
Source5853:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ionumbers.doc.tar.xz
Source6091:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyplain.tar.xz
Source6092:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyplain.doc.tar.xz
Source6401:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/icsv.tar.xz
Source6402:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/icsv.doc.tar.xz
Source6404:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ieeepes.tar.xz
Source6405:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ieeepes.doc.tar.xz
Source6406:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ijmart.tar.xz
Source6407:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ijmart.doc.tar.xz
Source6409:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/imac.tar.xz
Source6410:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/imac.doc.tar.xz
Source6411:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/imtekda.tar.xz
Source6412:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/imtekda.doc.tar.xz
Source6758:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/interchar.tar.xz
Source6759:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/interchar.doc.tar.xz
Source7375:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-bulgarian.doc.tar.xz
Source7376:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-churchslavonic.tar.xz
Source7379:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-occitan.tar.xz
Source7380:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-sanskrit.doc.tar.xz
Source7381:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-spanish.doc.tar.xz
Source7385:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ietfbibs.doc.tar.xz
Source7386:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iffont.tar.xz
Source7387:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/iffont.doc.tar.xz
Source7389:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/imfellenglish.tar.xz
Source7390:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/imfellenglish.doc.tar.xz
Source7781:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyphen-belarusian.tar.xz
Source7782:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifptex.tar.xz
Source7783:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifptex.doc.tar.xz
Source7784:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifxptex.tar.xz
Source7785:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ifxptex.doc.tar.xz
Source7786:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ijsra.tar.xz
Source7787:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ijsra.doc.tar.xz
Source7788:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/invoice2.tar.xz
Source7789:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/invoice2.doc.tar.xz
Source8174:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyperbar.tar.xz
Source8175:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hyperbar.doc.tar.xz
Source8176:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/includernw.tar.xz
Source8177:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/includernw.doc.tar.xz
Source8178:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/intopdf.tar.xz
Source8179:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/intopdf.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-hyph-utf8
Provides:       tex-hyph-utf8 = %{tl_version}
License:        Copyright only
Summary:        Hyphenation patterns expressed in UTF-8
Version:        svn48290
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(conv-utf8-ec.tex) = %{tl_version}, tex(conv-utf8-il2.tex) = %{tl_version}
Provides:       tex(conv-utf8-il3.tex) = %{tl_version}, tex(conv-utf8-l7x.tex) = %{tl_version}
Provides:       tex(conv-utf8-lmc.tex) = %{tl_version}, tex(conv-utf8-lth.tex) = %{tl_version}
Provides:       tex(conv-utf8-qx.tex) = %{tl_version}, tex(conv-utf8-t2a.tex) = %{tl_version}
Provides:       tex(conv-utf8-t8m.tex) = %{tl_version}

%description -n texlive-hyph-utf8
Modern native UTF-8 engines such as XeTeX and LuaTeX need
hyphenation patterns in UTF-8 format, whereas older systems
require hyphenation patterns in the 8-bit encoding of the font
in use (such encodings are codified in the LaTeX scheme with
names like OT1, T2A, TS1, OML, LY1, etc). The present package
offers a collection of conversions of existing patterns to UTF-
8 format, together with converters for use with 8-bit fonts in
older systems. Since hyphenation patterns for Knuthian-style
TeX systems are only read at iniTeX time, it is hoped that the
UTF-8 patterns, with their converters, will completely supplant
the older patterns.

%package -n texlive-hyph-utf8-doc
Summary:        Documentation for hyph-utf8
Version:        svn48290
Provides:       tex-hyph-utf8-doc
AutoReqProv:    No

%description -n texlive-hyph-utf8-doc
Documentation for hyph-utf8

%package -n texlive-hyphen-base
Provides:       tex-hyphen-base = %{tl_version}
License:        LPPL
Summary:        hyphen-base package
Version:        svn48303
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(language.dat) = %{tl_version}, tex(language.def) = %{tl_version}
Provides:       tex(language.us.def) = %{tl_version}, tex(dumyhyph.tex) = %{tl_version}
Provides:       tex(hyphen.tex) = %{tl_version}, tex(hypht1.tex) = %{tl_version}
Provides:       tex(zerohyph.tex) = %{tl_version}

%description -n texlive-hyphen-base
hyphen-base package

%package -n texlive-ifluatex
Provides:       tex-ifluatex = %{tl_version}
License:        LPPL 1.3
Summary:        Provides the \ifluatex switch
Version:        svn47293
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(ifluatex.sty) = %{tl_version}

%description -n texlive-ifluatex
The package looks for LuaTeX regardless of its mode and
provides the switch \ifluatex; it works with Plain TeX or
LaTeX. The package is part of the oberdiek bundle.

%package -n texlive-ifluatex-doc
Summary:        Documentation for ifluatex
Version:        svn47293
Provides:       tex-ifluatex-doc
AutoReqProv:    No

%description -n texlive-ifluatex-doc
Documentation for ifluatex

%package -n texlive-ifxetex
Provides:       tex-ifxetex = %{tl_version}
License:        LPPL
Summary:        Am I running under XeTeX?
Version:        svn19685.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ifxetex.sty) = %{tl_version}

%description -n texlive-ifxetex
A simple package which provides an \ifxetex conditional, so
that other code can determine that it is running under XeTeX.
The package requires the e-TeX extensions to the TeX primitive
set.

%package -n texlive-ifxetex-doc
Summary:        Documentation for ifxetex
Version:        svn19685.0.5

Provides:       tex-ifxetex-doc
AutoReqProv:    No

%description -n texlive-ifxetex-doc
Documentation for ifxetex

%package -n texlive-hyperref
Provides:       tex-hyperref = %{tl_version}
License:        LPPL
Summary:        Extensive support for hypertext in LaTeX
Version:        svn46583
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(kvoptions.sty), tex(kvsetkeys.sty), tex(ltxcmds.sty), tex(rerunfilecheck.sty)
Requires:       tex(hobsub-hyperref.sty), tex(ifpdf.sty)
Requires:       tex(pdftexcmds.sty), tex(infwarerr.sty), tex(keyval.sty), tex(kvdefinekeys.sty)
Requires:       tex(pdfescape.sty), tex(ifvtex.sty), tex(ifxetex.sty), tex(hycolor.sty)
Requires:       tex(letltxmacro.sty), tex(auxhook.sty), tex(intcalc.sty), tex(etexcmds.sty)
Requires:       tex(memhfixc.sty), tex(stringenc.sty), tex(color.sty), tex(url.sty)
Requires:       tex(bitset.sty), tex(atbegshi.sty), tex(refcount.sty), tex(gettitlestring.sty)
Requires:       tex(pzdr.tfm)
Provides:       tex(backref.sty) = %{tl_version}, tex(hdvipdfm.def) = %{tl_version}
Provides:       tex(hdvips.def) = %{tl_version}, tex(hdvipson.def) = %{tl_version}
Provides:       tex(hdviwind.def) = %{tl_version}, tex(hpdftex.def) = %{tl_version}
Provides:       tex(htex4ht.cfg) = %{tl_version}, tex(htex4ht.def) = %{tl_version}
Provides:       tex(htexture.def) = %{tl_version}, tex(hvtex.def) = %{tl_version}
Provides:       tex(hvtexhtm.def) = %{tl_version}, tex(hvtexmrk.def) = %{tl_version}
Provides:       tex(hxetex.def) = %{tl_version}, tex(hyperref.sty) = %{tl_version}
Provides:       tex(hypertex.def) = %{tl_version}, tex(minitoc-hyper.sty) = %{tl_version}
Provides:       tex(minitoc.sty) = %{tl_version}, tex(nameref.sty) = %{tl_version}
Provides:       tex(nohyperref.sty) = %{tl_version}, tex(ntheorem-hyper.sty) = %{tl_version}
Provides:       tex(pd1enc.def) = %{tl_version}, tex(pdfmark.def) = %{tl_version}
Provides:       tex(psdextra.def) = %{tl_version}, tex(puarenc.def) = %{tl_version}
Provides:       tex(puenc.def) = %{tl_version}, tex(puvnenc.def) = %{tl_version}
Provides:       tex(xr-hyper.sty) = %{tl_version}

%description -n texlive-hyperref
The hyperref package is used to handle cross-referencing
commands in LaTeX to produce hypertext links in the document.
The package provides backends for the \special set defined for
HyperTeX DVI processors; for embedded pdfmark commands for
processing by Acrobat Distiller (dvips and Y&Y's dvipsone); for
Y&Y's dviwindo; for PDF control within pdfTeX and dvipdfm; for
TeX4ht; and for VTeX's pdf and HTML backends. The package is
distributed with the backref and nameref packages, which make
use of the facilities of hyperref. The package depends on the
author's kvoptions, ltxcmdsand refcount packages.

%package -n texlive-hyperref-doc
Summary:        Documentation for hyperref
Version:        svn46583
Provides:       tex-hyperref-doc
AutoReqProv:    No

%description -n texlive-hyperref-doc
Documentation for hyperref


%package -n texlive-ijqc
Provides:       tex-ijqc = %{tl_version}
License:        LPPL
Summary:        BibTeX style file for the Intl. J. Quantum Chem
Version:        svn15878.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-ijqc
ijqc.bst is a BibTeX style file to support publication in
Wiley's International Journal of Quantum Chemistry. It is not
in any way officially endorsed by the publisher or editors, and
is provided without any warranty one could ever think of.

%package -n texlive-ijqc-doc
Summary:        Documentation for ijqc
Version:        svn15878.1.2

Provides:       tex-ijqc-doc
AutoReqProv:    No

%description -n texlive-ijqc-doc
Documentation for ijqc

%package -n texlive-inlinebib
Provides:       tex-inlinebib = %{tl_version}
License:        LPPL
Summary:        Citations in footnotes
Version:        svn22018.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(inlinebib.sty) = %{tl_version}, tex(pageranges.sty) = %{tl_version}

%description -n texlive-inlinebib
A BibTeX style and a LaTeX package that allow for a full
bibliography at the end of the document as well as citation
details in footnotes. The footnote details include "op. cit."
and "ibid." contractions.

%package -n texlive-inlinebib-doc
Summary:        Documentation for inlinebib
Version:        svn22018.0

Provides:       tex-inlinebib-doc
AutoReqProv:    No

%description -n texlive-inlinebib-doc
Documentation for inlinebib

%package -n texlive-iopart-num
Provides:       tex-iopart-num = %{tl_version}
License:        LPPL
Summary:        Numeric citation style for IOP journals
Version:        svn15878.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-iopart-num
A BibTeX style providing numeric citation in Harvard-like
format. Intended for use with Institute of Physics (IOP)
journals, including Journal of Physics.

%package -n texlive-iopart-num-doc
Summary:        Documentation for iopart-num
Version:        svn15878.2.1

Provides:       tex-iopart-num-doc
AutoReqProv:    No

%description -n texlive-iopart-num-doc
Documentation for iopart-num

%package -n texlive-hyphenex
Provides:       tex-hyphenex = %{tl_version}
License:        Public Domain
Summary:        US English hyphenation exceptions file
Version:        svn37354.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ushyphex.tex) = %{tl_version}

%description -n texlive-hyphenex
Exceptions for American English hyphenation patterns are
occasionally published in the TeX User Group journal TUGboat.
This bundle provides alternative Perl and Bourne shell scripts
to convert the source of such an article into an exceptions
file, together with a recent copy of the article and machine-
readable files.

%package -n texlive-ifsym
Provides:       tex-ifsym = %{tl_version}
License:        LPPL
Summary:        A collection of symbols
Version:        svn24868.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty)
Provides:       tex(ifclk10.tfm) = %{tl_version}, tex(ifclkb10.tfm) = %{tl_version}
Provides:       tex(ifgeo10.tfm) = %{tl_version}, tex(ifgeob10.tfm) = %{tl_version}
Provides:       tex(ifgeobn10.tfm) = %{tl_version}, tex(ifgeobw10.tfm) = %{tl_version}
Provides:       tex(ifgeon10.tfm) = %{tl_version}, tex(ifgeow10.tfm) = %{tl_version}
Provides:       tex(ifsym10.tfm) = %{tl_version}, tex(ifsymb10.tfm) = %{tl_version}
Provides:       tex(ifsymbi10.tfm) = %{tl_version}, tex(ifsymi10.tfm) = %{tl_version}
Provides:       tex(ifwea10.tfm) = %{tl_version}, tex(ifweab10.tfm) = %{tl_version}
Provides:       tex(ifsym.sty) = %{tl_version}, tex(uifblk.fd) = %{tl_version}
Provides:       tex(uifclk.fd) = %{tl_version}, tex(uifgeo.fd) = %{tl_version}
Provides:       tex(uifsym.fd) = %{tl_version}, tex(uifwea.fd) = %{tl_version}

%description -n texlive-ifsym
A set of symbol fonts, written in Metafont, offering
(respectively) clock-face symbols, geometrical symbols, weather
symbols, mountaineering symbols, electronic circuit symbols and
a set of miscellaneous symbols. A LaTeX package is provided,
that allows the user to load only those symbols needed in a
document.

%package -n texlive-ifsym-doc
Summary:        Documentation for ifsym
Version:        svn24868.0

Provides:       tex-ifsym-doc
AutoReqProv:    No

%description -n texlive-ifsym-doc
Documentation for ifsym

%package -n texlive-inconsolata
Provides:       tex-inconsolata = %{tl_version}
License:        OFL
Summary:        A monospaced font, with support files for use with TeX
Version:        svn46319
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(textcomp.sty)
Requires:       tex(keyval.sty)
Provides:       tex(i4-ly1-0.enc) = %{tl_version}, tex(i4-ly1-1.enc) = %{tl_version}
Provides:       tex(i4-ly1-2.enc) = %{tl_version}, tex(i4-ly1-3.enc) = %{tl_version}
Provides:       tex(i4-ly1-4.enc) = %{tl_version}, tex(i4-ly1-5.enc) = %{tl_version}
Provides:       tex(i4-ly1-6.enc) = %{tl_version}, tex(i4-ly1-7.enc) = %{tl_version}
Provides:       tex(i4-ot1-0.enc) = %{tl_version}, tex(i4-ot1-1.enc) = %{tl_version}
Provides:       tex(i4-ot1-2.enc) = %{tl_version}, tex(i4-ot1-3.enc) = %{tl_version}
Provides:       tex(i4-ot1-4.enc) = %{tl_version}, tex(i4-ot1-5.enc) = %{tl_version}
Provides:       tex(i4-ot1-6.enc) = %{tl_version}, tex(i4-ot1-7.enc) = %{tl_version}
Provides:       tex(i4-qx-0.enc) = %{tl_version}, tex(i4-qx-1.enc) = %{tl_version}
Provides:       tex(i4-qx-2.enc) = %{tl_version}, tex(i4-qx-3.enc) = %{tl_version}
Provides:       tex(i4-qx-4.enc) = %{tl_version}, tex(i4-qx-5.enc) = %{tl_version}
Provides:       tex(i4-qx-6.enc) = %{tl_version}, tex(i4-qx-7.enc) = %{tl_version}
Provides:       tex(i4-t1-0.enc) = %{tl_version}, tex(i4-t1-1.enc) = %{tl_version}
Provides:       tex(i4-t1-2.enc) = %{tl_version}, tex(i4-t1-3.enc) = %{tl_version}
Provides:       tex(i4-t1-4.enc) = %{tl_version}, tex(i4-t1-5.enc) = %{tl_version}
Provides:       tex(i4-t1-6.enc) = %{tl_version}, tex(i4-t1-7.enc) = %{tl_version}
Provides:       tex(i4-ts1.enc) = %{tl_version}, tex(zi4.map) = %{tl_version}
Provides:       tex(Inconsolatazi4-Bold.otf) = %{tl_version}
Provides:       tex(Inconsolatazi4-Regular.otf) = %{tl_version}
Provides:       tex(ly1-zi4b-0.tfm) = %{tl_version}, tex(ly1-zi4b-1.tfm) = %{tl_version}
Provides:       tex(ly1-zi4b-2.tfm) = %{tl_version}, tex(ly1-zi4b-3.tfm) = %{tl_version}
Provides:       tex(ly1-zi4b-4.tfm) = %{tl_version}, tex(ly1-zi4b-5.tfm) = %{tl_version}
Provides:       tex(ly1-zi4b-6.tfm) = %{tl_version}, tex(ly1-zi4b-7.tfm) = %{tl_version}
Provides:       tex(ly1-zi4r-0.tfm) = %{tl_version}, tex(ly1-zi4r-1.tfm) = %{tl_version}
Provides:       tex(ly1-zi4r-2.tfm) = %{tl_version}, tex(ly1-zi4r-3.tfm) = %{tl_version}
Provides:       tex(ly1-zi4r-4.tfm) = %{tl_version}, tex(ly1-zi4r-5.tfm) = %{tl_version}
Provides:       tex(ly1-zi4r-6.tfm) = %{tl_version}, tex(ly1-zi4r-7.tfm) = %{tl_version}
Provides:       tex(ot1-zi4b-0.tfm) = %{tl_version}, tex(ot1-zi4b-1.tfm) = %{tl_version}
Provides:       tex(ot1-zi4b-2.tfm) = %{tl_version}, tex(ot1-zi4b-3.tfm) = %{tl_version}
Provides:       tex(ot1-zi4b-4.tfm) = %{tl_version}, tex(ot1-zi4b-5.tfm) = %{tl_version}
Provides:       tex(ot1-zi4b-6.tfm) = %{tl_version}, tex(ot1-zi4b-7.tfm) = %{tl_version}
Provides:       tex(ot1-zi4r-0.tfm) = %{tl_version}, tex(ot1-zi4r-1.tfm) = %{tl_version}
Provides:       tex(ot1-zi4r-2.tfm) = %{tl_version}, tex(ot1-zi4r-3.tfm) = %{tl_version}
Provides:       tex(ot1-zi4r-4.tfm) = %{tl_version}, tex(ot1-zi4r-5.tfm) = %{tl_version}
Provides:       tex(ot1-zi4r-6.tfm) = %{tl_version}, tex(ot1-zi4r-7.tfm) = %{tl_version}
Provides:       tex(qx-zi4b-0.tfm) = %{tl_version}, tex(qx-zi4b-1.tfm) = %{tl_version}
Provides:       tex(qx-zi4b-2.tfm) = %{tl_version}, tex(qx-zi4b-3.tfm) = %{tl_version}
Provides:       tex(qx-zi4b-4.tfm) = %{tl_version}, tex(qx-zi4b-5.tfm) = %{tl_version}
Provides:       tex(qx-zi4b-6.tfm) = %{tl_version}, tex(qx-zi4b-7.tfm) = %{tl_version}
Provides:       tex(qx-zi4r-0.tfm) = %{tl_version}, tex(qx-zi4r-1.tfm) = %{tl_version}
Provides:       tex(qx-zi4r-2.tfm) = %{tl_version}, tex(qx-zi4r-3.tfm) = %{tl_version}
Provides:       tex(qx-zi4r-4.tfm) = %{tl_version}, tex(qx-zi4r-5.tfm) = %{tl_version}
Provides:       tex(qx-zi4r-6.tfm) = %{tl_version}, tex(qx-zi4r-7.tfm) = %{tl_version}
Provides:       tex(t1-zi4b-0.tfm) = %{tl_version}, tex(t1-zi4b-1.tfm) = %{tl_version}
Provides:       tex(t1-zi4b-2.tfm) = %{tl_version}, tex(t1-zi4b-3.tfm) = %{tl_version}
Provides:       tex(t1-zi4b-4.tfm) = %{tl_version}, tex(t1-zi4b-5.tfm) = %{tl_version}
Provides:       tex(t1-zi4b-6.tfm) = %{tl_version}, tex(t1-zi4b-7.tfm) = %{tl_version}
Provides:       tex(t1-zi4r-0.tfm) = %{tl_version}, tex(t1-zi4r-1.tfm) = %{tl_version}
Provides:       tex(t1-zi4r-2.tfm) = %{tl_version}, tex(t1-zi4r-3.tfm) = %{tl_version}
Provides:       tex(t1-zi4r-4.tfm) = %{tl_version}, tex(t1-zi4r-5.tfm) = %{tl_version}
Provides:       tex(t1-zi4r-6.tfm) = %{tl_version}, tex(t1-zi4r-7.tfm) = %{tl_version}
Provides:       tex(ts1-zi4b.tfm) = %{tl_version}, tex(ts1-zi4r.tfm) = %{tl_version}
Provides:       tex(Inconsolata-zi4b.pfb) = %{tl_version}
Provides:       tex(Inconsolata-zi4r.pfb) = %{tl_version}
Provides:       tex(inconsolata.sty) = %{tl_version}, tex(ly1zi4.fd) = %{tl_version}
Provides:       tex(ot1zi4.fd) = %{tl_version}, tex(qxzi4.fd) = %{tl_version}
Provides:       tex(t1zi4.fd) = %{tl_version}, tex(ts1zi4.fd) = %{tl_version}
Provides:       tex(zi4.sty) = %{tl_version}

%description -n texlive-inconsolata
Inconsolata is a monospaced font designed by Raph Levien. This
package contains the font (in both Adobe Type 1 and OpenType
formats) in regular and bold weights, with additional glyphs
and options to control slashed zero, upright quotes and a
shapelier lower-case L, plus metric files for use with TeX, and
LaTeX font definition and other relevant files.

%package -n texlive-inconsolata-doc
Summary:        Documentation for inconsolata
Version:        svn46319
Provides:       tex-inconsolata-doc
AutoReqProv:    No

%description -n texlive-inconsolata-doc
Documentation for inconsolata

%package -n texlive-initials
Provides:       tex-initials = %{tl_version}
License:        LPPL
Summary:        Adobe Type 1 decorative initial fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(Acorn.map) = %{tl_version}, tex(AnnSton.map) = %{tl_version}
Provides:       tex(ArtNouv.map) = %{tl_version}, tex(ArtNouvc.map) = %{tl_version}
Provides:       tex(Carrickc.map) = %{tl_version}, tex(Eichenla.map) = %{tl_version}
Provides:       tex(Eileen.map) = %{tl_version}, tex(EileenBl.map) = %{tl_version}
Provides:       tex(Elzevier.map) = %{tl_version}, tex(GotIn.map) = %{tl_version}
Provides:       tex(GoudyIn.map) = %{tl_version}, tex(Kinigcap.map) = %{tl_version}
Provides:       tex(Konanur.map) = %{tl_version}, tex(Kramer.map) = %{tl_version}
Provides:       tex(MorrisIn.map) = %{tl_version}, tex(Nouveaud.map) = %{tl_version}
Provides:       tex(Romantik.map) = %{tl_version}, tex(Rothdn.map) = %{tl_version}
Provides:       tex(RoyalIn.map) = %{tl_version}, tex(Sanremo.map) = %{tl_version}
Provides:       tex(Starburst.map) = %{tl_version}, tex(Typocaps.map) = %{tl_version}
Provides:       tex(Zallman.map) = %{tl_version}, tex(Acorn.tfm) = %{tl_version}
Provides:       tex(AnnSton.tfm) = %{tl_version}, tex(ArtNouv.tfm) = %{tl_version}
Provides:       tex(ArtNouvc.tfm) = %{tl_version}, tex(Carrickc.tfm) = %{tl_version}
Provides:       tex(Eichenla.tfm) = %{tl_version}, tex(Eileen.tfm) = %{tl_version}
Provides:       tex(EileenBl.tfm) = %{tl_version}, tex(Elzevier.tfm) = %{tl_version}
Provides:       tex(GotIn.tfm) = %{tl_version}, tex(GoudyIn.tfm) = %{tl_version}
Provides:       tex(Kinigcap.tfm) = %{tl_version}, tex(Konanur.tfm) = %{tl_version}
Provides:       tex(Kramer.tfm) = %{tl_version}, tex(MorrisIn.tfm) = %{tl_version}
Provides:       tex(Nouveaud.tfm) = %{tl_version}, tex(Romantik.tfm) = %{tl_version}
Provides:       tex(Rothdn.tfm) = %{tl_version}, tex(RoyalIn.tfm) = %{tl_version}
Provides:       tex(Sanremo.tfm) = %{tl_version}, tex(Starburst.tfm) = %{tl_version}
Provides:       tex(Typocaps.tfm) = %{tl_version}, tex(Zallman.tfm) = %{tl_version}
Provides:       tex(Acorn.pfb) = %{tl_version}, tex(AnnSton.pfb) = %{tl_version}
Provides:       tex(ArtNouv.pfb) = %{tl_version}, tex(ArtNouvc.pfb) = %{tl_version}
Provides:       tex(Carrickc.pfb) = %{tl_version}, tex(Eichenla.pfb) = %{tl_version}
Provides:       tex(Eileen.pfb) = %{tl_version}, tex(EileenBl.pfb) = %{tl_version}
Provides:       tex(Elzevier.pfb) = %{tl_version}, tex(GotIn.pfb) = %{tl_version}
Provides:       tex(GoudyIn.pfb) = %{tl_version}, tex(Kinigcap.pfb) = %{tl_version}
Provides:       tex(Konanur.pfb) = %{tl_version}, tex(Kramer.pfb) = %{tl_version}
Provides:       tex(MorrisIn.pfb) = %{tl_version}, tex(Nouveaud.pfb) = %{tl_version}
Provides:       tex(Romantik.pfb) = %{tl_version}, tex(Rothdn.pfb) = %{tl_version}
Provides:       tex(RoyalIn.pfb) = %{tl_version}, tex(Sanremo.pfb) = %{tl_version}
Provides:       tex(Starburst.pfb) = %{tl_version}, tex(Typocaps.pfb) = %{tl_version}
Provides:       tex(Zallman.pfb) = %{tl_version}, tex(Acorn.fd) = %{tl_version}
Provides:       tex(AnnSton.fd) = %{tl_version}, tex(ArtNouv.fd) = %{tl_version}
Provides:       tex(ArtNouvc.fd) = %{tl_version}, tex(Carrickc.fd) = %{tl_version}
Provides:       tex(Eichenla.fd) = %{tl_version}, tex(Eileen.fd) = %{tl_version}
Provides:       tex(EileenBl.fd) = %{tl_version}, tex(Elzevier.fd) = %{tl_version}
Provides:       tex(GotIn.fd) = %{tl_version}, tex(GoudyIn.fd) = %{tl_version}
Provides:       tex(Kinigcap.fd) = %{tl_version}, tex(Konanur.fd) = %{tl_version}
Provides:       tex(Kramer.fd) = %{tl_version}, tex(MorrisIn.fd) = %{tl_version}
Provides:       tex(Nouveaud.fd) = %{tl_version}, tex(Romantik.fd) = %{tl_version}
Provides:       tex(Rothdn.fd) = %{tl_version}, tex(RoyalIn.fd) = %{tl_version}
Provides:       tex(Sanremo.fd) = %{tl_version}, tex(Starburst.fd) = %{tl_version}
Provides:       tex(Typocaps.fd) = %{tl_version}, tex(Zallman.fd) = %{tl_version}

%description -n texlive-initials
For each font, at least an .pfb and .tfm file is provided, with
a .fd file for use with LaTeX.

%package -n texlive-initials-doc
Summary:        Documentation for initials
Version:        svn15878.0

Provides:       tex-initials-doc
AutoReqProv:    No

%description -n texlive-initials-doc
Documentation for initials

%package -n texlive-ipaex-type1
Provides:       tex-ipaex-type1 = %{tl_version}
License:        IPA
Summary:        IPAex fonts converted to Type-1 format Unicode subfonts
Version:        svn47700
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       tex(ipaex-type1.map) = %{tl_version}, tex(ipxg-r-ot1.tfm) = %{tl_version}
Provides:       tex(ipxg-r-t1.tfm) = %{tl_version}, tex(ipxg-r-ts1.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u00.tfm) = %{tl_version}, tex(ipxg-r-u01.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u02.tfm) = %{tl_version}, tex(ipxg-r-u03.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u04.tfm) = %{tl_version}, tex(ipxg-r-u1e.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u1f.tfm) = %{tl_version}, tex(ipxg-r-u20.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u21.tfm) = %{tl_version}, tex(ipxg-r-u22.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u23.tfm) = %{tl_version}, tex(ipxg-r-u24.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u25.tfm) = %{tl_version}, tex(ipxg-r-u26.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u27.tfm) = %{tl_version}, tex(ipxg-r-u29.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u2e.tfm) = %{tl_version}, tex(ipxg-r-u2f.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u30.tfm) = %{tl_version}, tex(ipxg-r-u31.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u32.tfm) = %{tl_version}, tex(ipxg-r-u33.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u34.tfm) = %{tl_version}, tex(ipxg-r-u35.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u36.tfm) = %{tl_version}, tex(ipxg-r-u37.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u38.tfm) = %{tl_version}, tex(ipxg-r-u39.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u3a.tfm) = %{tl_version}, tex(ipxg-r-u3b.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u3c.tfm) = %{tl_version}, tex(ipxg-r-u3d.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u3e.tfm) = %{tl_version}, tex(ipxg-r-u3f.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u40.tfm) = %{tl_version}, tex(ipxg-r-u41.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u42.tfm) = %{tl_version}, tex(ipxg-r-u43.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u44.tfm) = %{tl_version}, tex(ipxg-r-u45.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u46.tfm) = %{tl_version}, tex(ipxg-r-u47.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u48.tfm) = %{tl_version}, tex(ipxg-r-u49.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u4a.tfm) = %{tl_version}, tex(ipxg-r-u4b.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u4c.tfm) = %{tl_version}, tex(ipxg-r-u4d.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u4e.tfm) = %{tl_version}, tex(ipxg-r-u4f.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u50.tfm) = %{tl_version}, tex(ipxg-r-u51.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u52.tfm) = %{tl_version}, tex(ipxg-r-u53.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u54.tfm) = %{tl_version}, tex(ipxg-r-u55.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u56.tfm) = %{tl_version}, tex(ipxg-r-u57.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u58.tfm) = %{tl_version}, tex(ipxg-r-u59.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u5a.tfm) = %{tl_version}, tex(ipxg-r-u5b.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u5c.tfm) = %{tl_version}, tex(ipxg-r-u5d.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u5e.tfm) = %{tl_version}, tex(ipxg-r-u5f.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u60.tfm) = %{tl_version}, tex(ipxg-r-u61.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u62.tfm) = %{tl_version}, tex(ipxg-r-u63.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u64.tfm) = %{tl_version}, tex(ipxg-r-u65.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u66.tfm) = %{tl_version}, tex(ipxg-r-u67.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u68.tfm) = %{tl_version}, tex(ipxg-r-u69.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u6a.tfm) = %{tl_version}, tex(ipxg-r-u6b.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u6c.tfm) = %{tl_version}, tex(ipxg-r-u6d.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u6e.tfm) = %{tl_version}, tex(ipxg-r-u6f.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u70.tfm) = %{tl_version}, tex(ipxg-r-u71.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u72.tfm) = %{tl_version}, tex(ipxg-r-u73.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u74.tfm) = %{tl_version}, tex(ipxg-r-u75.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u76.tfm) = %{tl_version}, tex(ipxg-r-u77.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u78.tfm) = %{tl_version}, tex(ipxg-r-u79.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u7a.tfm) = %{tl_version}, tex(ipxg-r-u7b.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u7c.tfm) = %{tl_version}, tex(ipxg-r-u7d.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u7e.tfm) = %{tl_version}, tex(ipxg-r-u7f.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u80.tfm) = %{tl_version}, tex(ipxg-r-u81.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u82.tfm) = %{tl_version}, tex(ipxg-r-u83.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u84.tfm) = %{tl_version}, tex(ipxg-r-u85.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u86.tfm) = %{tl_version}, tex(ipxg-r-u87.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u88.tfm) = %{tl_version}, tex(ipxg-r-u89.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u8a.tfm) = %{tl_version}, tex(ipxg-r-u8b.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u8c.tfm) = %{tl_version}, tex(ipxg-r-u8d.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u8e.tfm) = %{tl_version}, tex(ipxg-r-u8f.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u90.tfm) = %{tl_version}, tex(ipxg-r-u91.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u92.tfm) = %{tl_version}, tex(ipxg-r-u93.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u94.tfm) = %{tl_version}, tex(ipxg-r-u95.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u96.tfm) = %{tl_version}, tex(ipxg-r-u97.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u98.tfm) = %{tl_version}, tex(ipxg-r-u99.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u9a.tfm) = %{tl_version}, tex(ipxg-r-u9b.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u9c.tfm) = %{tl_version}, tex(ipxg-r-u9d.tfm) = %{tl_version}
Provides:       tex(ipxg-r-u9e.tfm) = %{tl_version}, tex(ipxg-r-u9f.tfm) = %{tl_version}
Provides:       tex(ipxg-r-uf0.tfm) = %{tl_version}, tex(ipxg-r-uf8.tfm) = %{tl_version}
Provides:       tex(ipxg-r-uf9.tfm) = %{tl_version}, tex(ipxg-r-ufa.tfm) = %{tl_version}
Provides:       tex(ipxg-r-ufe.tfm) = %{tl_version}, tex(ipxg-r-uff.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-ot1.tfm) = %{tl_version}, tex(ipxg-ro-t1.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-ts1.tfm) = %{tl_version}, tex(ipxg-ro-u00.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u01.tfm) = %{tl_version}, tex(ipxg-ro-u02.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u03.tfm) = %{tl_version}, tex(ipxg-ro-u04.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u1e.tfm) = %{tl_version}, tex(ipxg-ro-u1f.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u20.tfm) = %{tl_version}, tex(ipxg-ro-u21.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u22.tfm) = %{tl_version}, tex(ipxg-ro-u23.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u24.tfm) = %{tl_version}, tex(ipxg-ro-u25.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u26.tfm) = %{tl_version}, tex(ipxg-ro-u27.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u29.tfm) = %{tl_version}, tex(ipxg-ro-u2e.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u2f.tfm) = %{tl_version}, tex(ipxg-ro-u30.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u31.tfm) = %{tl_version}, tex(ipxg-ro-u32.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u33.tfm) = %{tl_version}, tex(ipxg-ro-u34.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u35.tfm) = %{tl_version}, tex(ipxg-ro-u36.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u37.tfm) = %{tl_version}, tex(ipxg-ro-u38.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u39.tfm) = %{tl_version}, tex(ipxg-ro-u3a.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u3b.tfm) = %{tl_version}, tex(ipxg-ro-u3c.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u3d.tfm) = %{tl_version}, tex(ipxg-ro-u3e.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u3f.tfm) = %{tl_version}, tex(ipxg-ro-u40.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u41.tfm) = %{tl_version}, tex(ipxg-ro-u42.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u43.tfm) = %{tl_version}, tex(ipxg-ro-u44.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u45.tfm) = %{tl_version}, tex(ipxg-ro-u46.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u47.tfm) = %{tl_version}, tex(ipxg-ro-u48.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u49.tfm) = %{tl_version}, tex(ipxg-ro-u4a.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u4b.tfm) = %{tl_version}, tex(ipxg-ro-u4c.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u4d.tfm) = %{tl_version}, tex(ipxg-ro-u4e.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u4f.tfm) = %{tl_version}, tex(ipxg-ro-u50.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u51.tfm) = %{tl_version}, tex(ipxg-ro-u52.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u53.tfm) = %{tl_version}, tex(ipxg-ro-u54.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u55.tfm) = %{tl_version}, tex(ipxg-ro-u56.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u57.tfm) = %{tl_version}, tex(ipxg-ro-u58.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u59.tfm) = %{tl_version}, tex(ipxg-ro-u5a.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u5b.tfm) = %{tl_version}, tex(ipxg-ro-u5c.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u5d.tfm) = %{tl_version}, tex(ipxg-ro-u5e.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u5f.tfm) = %{tl_version}, tex(ipxg-ro-u60.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u61.tfm) = %{tl_version}, tex(ipxg-ro-u62.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u63.tfm) = %{tl_version}, tex(ipxg-ro-u64.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u65.tfm) = %{tl_version}, tex(ipxg-ro-u66.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u67.tfm) = %{tl_version}, tex(ipxg-ro-u68.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u69.tfm) = %{tl_version}, tex(ipxg-ro-u6a.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u6b.tfm) = %{tl_version}, tex(ipxg-ro-u6c.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u6d.tfm) = %{tl_version}, tex(ipxg-ro-u6e.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u6f.tfm) = %{tl_version}, tex(ipxg-ro-u70.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u71.tfm) = %{tl_version}, tex(ipxg-ro-u72.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u73.tfm) = %{tl_version}, tex(ipxg-ro-u74.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u75.tfm) = %{tl_version}, tex(ipxg-ro-u76.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u77.tfm) = %{tl_version}, tex(ipxg-ro-u78.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u79.tfm) = %{tl_version}, tex(ipxg-ro-u7a.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u7b.tfm) = %{tl_version}, tex(ipxg-ro-u7c.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u7d.tfm) = %{tl_version}, tex(ipxg-ro-u7e.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u7f.tfm) = %{tl_version}, tex(ipxg-ro-u80.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u81.tfm) = %{tl_version}, tex(ipxg-ro-u82.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u83.tfm) = %{tl_version}, tex(ipxg-ro-u84.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u85.tfm) = %{tl_version}, tex(ipxg-ro-u86.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u87.tfm) = %{tl_version}, tex(ipxg-ro-u88.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u89.tfm) = %{tl_version}, tex(ipxg-ro-u8a.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u8b.tfm) = %{tl_version}, tex(ipxg-ro-u8c.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u8d.tfm) = %{tl_version}, tex(ipxg-ro-u8e.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u8f.tfm) = %{tl_version}, tex(ipxg-ro-u90.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u91.tfm) = %{tl_version}, tex(ipxg-ro-u92.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u93.tfm) = %{tl_version}, tex(ipxg-ro-u94.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u95.tfm) = %{tl_version}, tex(ipxg-ro-u96.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u97.tfm) = %{tl_version}, tex(ipxg-ro-u98.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u99.tfm) = %{tl_version}, tex(ipxg-ro-u9a.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u9b.tfm) = %{tl_version}, tex(ipxg-ro-u9c.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u9d.tfm) = %{tl_version}, tex(ipxg-ro-u9e.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-u9f.tfm) = %{tl_version}, tex(ipxg-ro-uf8.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-uf9.tfm) = %{tl_version}, tex(ipxg-ro-ufa.tfm) = %{tl_version}
Provides:       tex(ipxg-ro-ufe.tfm) = %{tl_version}, tex(ipxg-ro-uff.tfm) = %{tl_version}
Provides:       tex(ipxm-r-ot1.tfm) = %{tl_version}, tex(ipxm-r-t1.tfm) = %{tl_version}
Provides:       tex(ipxm-r-ts1.tfm) = %{tl_version}, tex(ipxm-r-u00.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u01.tfm) = %{tl_version}, tex(ipxm-r-u02.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u03.tfm) = %{tl_version}, tex(ipxm-r-u04.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u1e.tfm) = %{tl_version}, tex(ipxm-r-u1f.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u20.tfm) = %{tl_version}, tex(ipxm-r-u21.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u22.tfm) = %{tl_version}, tex(ipxm-r-u23.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u24.tfm) = %{tl_version}, tex(ipxm-r-u25.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u26.tfm) = %{tl_version}, tex(ipxm-r-u27.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u29.tfm) = %{tl_version}, tex(ipxm-r-u2e.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u2f.tfm) = %{tl_version}, tex(ipxm-r-u30.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u31.tfm) = %{tl_version}, tex(ipxm-r-u32.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u33.tfm) = %{tl_version}, tex(ipxm-r-u34.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u35.tfm) = %{tl_version}, tex(ipxm-r-u36.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u37.tfm) = %{tl_version}, tex(ipxm-r-u38.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u39.tfm) = %{tl_version}, tex(ipxm-r-u3a.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u3b.tfm) = %{tl_version}, tex(ipxm-r-u3c.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u3d.tfm) = %{tl_version}, tex(ipxm-r-u3e.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u3f.tfm) = %{tl_version}, tex(ipxm-r-u40.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u41.tfm) = %{tl_version}, tex(ipxm-r-u42.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u43.tfm) = %{tl_version}, tex(ipxm-r-u44.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u45.tfm) = %{tl_version}, tex(ipxm-r-u46.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u47.tfm) = %{tl_version}, tex(ipxm-r-u48.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u49.tfm) = %{tl_version}, tex(ipxm-r-u4a.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u4b.tfm) = %{tl_version}, tex(ipxm-r-u4c.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u4d.tfm) = %{tl_version}, tex(ipxm-r-u4e.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u4f.tfm) = %{tl_version}, tex(ipxm-r-u50.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u51.tfm) = %{tl_version}, tex(ipxm-r-u52.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u53.tfm) = %{tl_version}, tex(ipxm-r-u54.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u55.tfm) = %{tl_version}, tex(ipxm-r-u56.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u57.tfm) = %{tl_version}, tex(ipxm-r-u58.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u59.tfm) = %{tl_version}, tex(ipxm-r-u5a.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u5b.tfm) = %{tl_version}, tex(ipxm-r-u5c.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u5d.tfm) = %{tl_version}, tex(ipxm-r-u5e.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u5f.tfm) = %{tl_version}, tex(ipxm-r-u60.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u61.tfm) = %{tl_version}, tex(ipxm-r-u62.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u63.tfm) = %{tl_version}, tex(ipxm-r-u64.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u65.tfm) = %{tl_version}, tex(ipxm-r-u66.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u67.tfm) = %{tl_version}, tex(ipxm-r-u68.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u69.tfm) = %{tl_version}, tex(ipxm-r-u6a.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u6b.tfm) = %{tl_version}, tex(ipxm-r-u6c.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u6d.tfm) = %{tl_version}, tex(ipxm-r-u6e.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u6f.tfm) = %{tl_version}, tex(ipxm-r-u70.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u71.tfm) = %{tl_version}, tex(ipxm-r-u72.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u73.tfm) = %{tl_version}, tex(ipxm-r-u74.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u75.tfm) = %{tl_version}, tex(ipxm-r-u76.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u77.tfm) = %{tl_version}, tex(ipxm-r-u78.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u79.tfm) = %{tl_version}, tex(ipxm-r-u7a.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u7b.tfm) = %{tl_version}, tex(ipxm-r-u7c.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u7d.tfm) = %{tl_version}, tex(ipxm-r-u7e.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u7f.tfm) = %{tl_version}, tex(ipxm-r-u80.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u81.tfm) = %{tl_version}, tex(ipxm-r-u82.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u83.tfm) = %{tl_version}, tex(ipxm-r-u84.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u85.tfm) = %{tl_version}, tex(ipxm-r-u86.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u87.tfm) = %{tl_version}, tex(ipxm-r-u88.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u89.tfm) = %{tl_version}, tex(ipxm-r-u8a.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u8b.tfm) = %{tl_version}, tex(ipxm-r-u8c.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u8d.tfm) = %{tl_version}, tex(ipxm-r-u8e.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u8f.tfm) = %{tl_version}, tex(ipxm-r-u90.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u91.tfm) = %{tl_version}, tex(ipxm-r-u92.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u93.tfm) = %{tl_version}, tex(ipxm-r-u94.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u95.tfm) = %{tl_version}, tex(ipxm-r-u96.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u97.tfm) = %{tl_version}, tex(ipxm-r-u98.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u99.tfm) = %{tl_version}, tex(ipxm-r-u9a.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u9b.tfm) = %{tl_version}, tex(ipxm-r-u9c.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u9d.tfm) = %{tl_version}, tex(ipxm-r-u9e.tfm) = %{tl_version}
Provides:       tex(ipxm-r-u9f.tfm) = %{tl_version}, tex(ipxm-r-uf0.tfm) = %{tl_version}
Provides:       tex(ipxm-r-uf8.tfm) = %{tl_version}, tex(ipxm-r-uf9.tfm) = %{tl_version}
Provides:       tex(ipxm-r-ufa.tfm) = %{tl_version}, tex(ipxm-r-ufe.tfm) = %{tl_version}
Provides:       tex(ipxm-r-uff.tfm) = %{tl_version}, tex(ipxm-ro-ot1.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-t1.tfm) = %{tl_version}, tex(ipxm-ro-ts1.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u00.tfm) = %{tl_version}, tex(ipxm-ro-u01.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u02.tfm) = %{tl_version}, tex(ipxm-ro-u03.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u04.tfm) = %{tl_version}, tex(ipxm-ro-u1e.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u1f.tfm) = %{tl_version}, tex(ipxm-ro-u20.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u21.tfm) = %{tl_version}, tex(ipxm-ro-u22.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u23.tfm) = %{tl_version}, tex(ipxm-ro-u24.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u25.tfm) = %{tl_version}, tex(ipxm-ro-u26.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u27.tfm) = %{tl_version}, tex(ipxm-ro-u29.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u2e.tfm) = %{tl_version}, tex(ipxm-ro-u2f.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u30.tfm) = %{tl_version}, tex(ipxm-ro-u31.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u32.tfm) = %{tl_version}, tex(ipxm-ro-u33.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u34.tfm) = %{tl_version}, tex(ipxm-ro-u35.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u36.tfm) = %{tl_version}, tex(ipxm-ro-u37.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u38.tfm) = %{tl_version}, tex(ipxm-ro-u39.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u3a.tfm) = %{tl_version}, tex(ipxm-ro-u3b.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u3c.tfm) = %{tl_version}, tex(ipxm-ro-u3d.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u3e.tfm) = %{tl_version}, tex(ipxm-ro-u3f.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u40.tfm) = %{tl_version}, tex(ipxm-ro-u41.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u42.tfm) = %{tl_version}, tex(ipxm-ro-u43.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u44.tfm) = %{tl_version}, tex(ipxm-ro-u45.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u46.tfm) = %{tl_version}, tex(ipxm-ro-u47.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u48.tfm) = %{tl_version}, tex(ipxm-ro-u49.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u4a.tfm) = %{tl_version}, tex(ipxm-ro-u4b.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u4c.tfm) = %{tl_version}, tex(ipxm-ro-u4d.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u4e.tfm) = %{tl_version}, tex(ipxm-ro-u4f.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u50.tfm) = %{tl_version}, tex(ipxm-ro-u51.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u52.tfm) = %{tl_version}, tex(ipxm-ro-u53.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u54.tfm) = %{tl_version}, tex(ipxm-ro-u55.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u56.tfm) = %{tl_version}, tex(ipxm-ro-u57.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u58.tfm) = %{tl_version}, tex(ipxm-ro-u59.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u5a.tfm) = %{tl_version}, tex(ipxm-ro-u5b.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u5c.tfm) = %{tl_version}, tex(ipxm-ro-u5d.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u5e.tfm) = %{tl_version}, tex(ipxm-ro-u5f.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u60.tfm) = %{tl_version}, tex(ipxm-ro-u61.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u62.tfm) = %{tl_version}, tex(ipxm-ro-u63.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u64.tfm) = %{tl_version}, tex(ipxm-ro-u65.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u66.tfm) = %{tl_version}, tex(ipxm-ro-u67.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u68.tfm) = %{tl_version}, tex(ipxm-ro-u69.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u6a.tfm) = %{tl_version}, tex(ipxm-ro-u6b.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u6c.tfm) = %{tl_version}, tex(ipxm-ro-u6d.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u6e.tfm) = %{tl_version}, tex(ipxm-ro-u6f.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u70.tfm) = %{tl_version}, tex(ipxm-ro-u71.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u72.tfm) = %{tl_version}, tex(ipxm-ro-u73.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u74.tfm) = %{tl_version}, tex(ipxm-ro-u75.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u76.tfm) = %{tl_version}, tex(ipxm-ro-u77.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u78.tfm) = %{tl_version}, tex(ipxm-ro-u79.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u7a.tfm) = %{tl_version}, tex(ipxm-ro-u7b.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u7c.tfm) = %{tl_version}, tex(ipxm-ro-u7d.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u7e.tfm) = %{tl_version}, tex(ipxm-ro-u7f.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u80.tfm) = %{tl_version}, tex(ipxm-ro-u81.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u82.tfm) = %{tl_version}, tex(ipxm-ro-u83.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u84.tfm) = %{tl_version}, tex(ipxm-ro-u85.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u86.tfm) = %{tl_version}, tex(ipxm-ro-u87.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u88.tfm) = %{tl_version}, tex(ipxm-ro-u89.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u8a.tfm) = %{tl_version}, tex(ipxm-ro-u8b.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u8c.tfm) = %{tl_version}, tex(ipxm-ro-u8d.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u8e.tfm) = %{tl_version}, tex(ipxm-ro-u8f.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u90.tfm) = %{tl_version}, tex(ipxm-ro-u91.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u92.tfm) = %{tl_version}, tex(ipxm-ro-u93.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u94.tfm) = %{tl_version}, tex(ipxm-ro-u95.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u96.tfm) = %{tl_version}, tex(ipxm-ro-u97.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u98.tfm) = %{tl_version}, tex(ipxm-ro-u99.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u9a.tfm) = %{tl_version}, tex(ipxm-ro-u9b.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u9c.tfm) = %{tl_version}, tex(ipxm-ro-u9d.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-u9e.tfm) = %{tl_version}, tex(ipxm-ro-u9f.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-uf8.tfm) = %{tl_version}, tex(ipxm-ro-uf9.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-ufa.tfm) = %{tl_version}, tex(ipxm-ro-ufe.tfm) = %{tl_version}
Provides:       tex(ipxm-ro-uff.tfm) = %{tl_version}, tex(ipxg-r-ot1.pfb) = %{tl_version}
Provides:       tex(ipxg-r-t1.pfb) = %{tl_version}, tex(ipxg-r-ts1.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u00.pfb) = %{tl_version}, tex(ipxg-r-u01.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u02.pfb) = %{tl_version}, tex(ipxg-r-u03.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u04.pfb) = %{tl_version}, tex(ipxg-r-u1e.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u1f.pfb) = %{tl_version}, tex(ipxg-r-u20.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u21.pfb) = %{tl_version}, tex(ipxg-r-u22.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u23.pfb) = %{tl_version}, tex(ipxg-r-u24.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u25.pfb) = %{tl_version}, tex(ipxg-r-u26.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u27.pfb) = %{tl_version}, tex(ipxg-r-u29.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u2e.pfb) = %{tl_version}, tex(ipxg-r-u2f.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u30.pfb) = %{tl_version}, tex(ipxg-r-u31.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u32.pfb) = %{tl_version}, tex(ipxg-r-u33.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u34.pfb) = %{tl_version}, tex(ipxg-r-u35.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u36.pfb) = %{tl_version}, tex(ipxg-r-u37.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u38.pfb) = %{tl_version}, tex(ipxg-r-u39.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u3a.pfb) = %{tl_version}, tex(ipxg-r-u3b.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u3c.pfb) = %{tl_version}, tex(ipxg-r-u3d.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u3e.pfb) = %{tl_version}, tex(ipxg-r-u3f.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u40.pfb) = %{tl_version}, tex(ipxg-r-u41.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u42.pfb) = %{tl_version}, tex(ipxg-r-u43.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u44.pfb) = %{tl_version}, tex(ipxg-r-u45.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u46.pfb) = %{tl_version}, tex(ipxg-r-u47.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u48.pfb) = %{tl_version}, tex(ipxg-r-u49.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u4a.pfb) = %{tl_version}, tex(ipxg-r-u4b.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u4c.pfb) = %{tl_version}, tex(ipxg-r-u4d.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u4e.pfb) = %{tl_version}, tex(ipxg-r-u4f.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u50.pfb) = %{tl_version}, tex(ipxg-r-u51.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u52.pfb) = %{tl_version}, tex(ipxg-r-u53.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u54.pfb) = %{tl_version}, tex(ipxg-r-u55.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u56.pfb) = %{tl_version}, tex(ipxg-r-u57.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u58.pfb) = %{tl_version}, tex(ipxg-r-u59.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u5a.pfb) = %{tl_version}, tex(ipxg-r-u5b.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u5c.pfb) = %{tl_version}, tex(ipxg-r-u5d.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u5e.pfb) = %{tl_version}, tex(ipxg-r-u5f.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u60.pfb) = %{tl_version}, tex(ipxg-r-u61.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u62.pfb) = %{tl_version}, tex(ipxg-r-u63.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u64.pfb) = %{tl_version}, tex(ipxg-r-u65.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u66.pfb) = %{tl_version}, tex(ipxg-r-u67.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u68.pfb) = %{tl_version}, tex(ipxg-r-u69.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u6a.pfb) = %{tl_version}, tex(ipxg-r-u6b.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u6c.pfb) = %{tl_version}, tex(ipxg-r-u6d.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u6e.pfb) = %{tl_version}, tex(ipxg-r-u6f.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u70.pfb) = %{tl_version}, tex(ipxg-r-u71.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u72.pfb) = %{tl_version}, tex(ipxg-r-u73.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u74.pfb) = %{tl_version}, tex(ipxg-r-u75.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u76.pfb) = %{tl_version}, tex(ipxg-r-u77.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u78.pfb) = %{tl_version}, tex(ipxg-r-u79.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u7a.pfb) = %{tl_version}, tex(ipxg-r-u7b.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u7c.pfb) = %{tl_version}, tex(ipxg-r-u7d.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u7e.pfb) = %{tl_version}, tex(ipxg-r-u7f.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u80.pfb) = %{tl_version}, tex(ipxg-r-u81.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u82.pfb) = %{tl_version}, tex(ipxg-r-u83.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u84.pfb) = %{tl_version}, tex(ipxg-r-u85.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u86.pfb) = %{tl_version}, tex(ipxg-r-u87.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u88.pfb) = %{tl_version}, tex(ipxg-r-u89.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u8a.pfb) = %{tl_version}, tex(ipxg-r-u8b.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u8c.pfb) = %{tl_version}, tex(ipxg-r-u8d.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u8e.pfb) = %{tl_version}, tex(ipxg-r-u8f.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u90.pfb) = %{tl_version}, tex(ipxg-r-u91.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u92.pfb) = %{tl_version}, tex(ipxg-r-u93.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u94.pfb) = %{tl_version}, tex(ipxg-r-u95.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u96.pfb) = %{tl_version}, tex(ipxg-r-u97.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u98.pfb) = %{tl_version}, tex(ipxg-r-u99.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u9a.pfb) = %{tl_version}, tex(ipxg-r-u9b.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u9c.pfb) = %{tl_version}, tex(ipxg-r-u9d.pfb) = %{tl_version}
Provides:       tex(ipxg-r-u9e.pfb) = %{tl_version}, tex(ipxg-r-u9f.pfb) = %{tl_version}
Provides:       tex(ipxg-r-uf0.pfb) = %{tl_version}, tex(ipxg-r-uf8.pfb) = %{tl_version}
Provides:       tex(ipxg-r-uf9.pfb) = %{tl_version}, tex(ipxg-r-ufa.pfb) = %{tl_version}
Provides:       tex(ipxg-r-ufe.pfb) = %{tl_version}, tex(ipxg-r-uff.pfb) = %{tl_version}
Provides:       tex(ipxm-r-ot1.pfb) = %{tl_version}, tex(ipxm-r-t1.pfb) = %{tl_version}
Provides:       tex(ipxm-r-ts1.pfb) = %{tl_version}, tex(ipxm-r-u00.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u01.pfb) = %{tl_version}, tex(ipxm-r-u02.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u03.pfb) = %{tl_version}, tex(ipxm-r-u04.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u1e.pfb) = %{tl_version}, tex(ipxm-r-u1f.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u20.pfb) = %{tl_version}, tex(ipxm-r-u21.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u22.pfb) = %{tl_version}, tex(ipxm-r-u23.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u24.pfb) = %{tl_version}, tex(ipxm-r-u25.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u26.pfb) = %{tl_version}, tex(ipxm-r-u27.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u29.pfb) = %{tl_version}, tex(ipxm-r-u2e.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u2f.pfb) = %{tl_version}, tex(ipxm-r-u30.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u31.pfb) = %{tl_version}, tex(ipxm-r-u32.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u33.pfb) = %{tl_version}, tex(ipxm-r-u34.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u35.pfb) = %{tl_version}, tex(ipxm-r-u36.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u37.pfb) = %{tl_version}, tex(ipxm-r-u38.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u39.pfb) = %{tl_version}, tex(ipxm-r-u3a.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u3b.pfb) = %{tl_version}, tex(ipxm-r-u3c.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u3d.pfb) = %{tl_version}, tex(ipxm-r-u3e.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u3f.pfb) = %{tl_version}, tex(ipxm-r-u40.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u41.pfb) = %{tl_version}, tex(ipxm-r-u42.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u43.pfb) = %{tl_version}, tex(ipxm-r-u44.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u45.pfb) = %{tl_version}, tex(ipxm-r-u46.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u47.pfb) = %{tl_version}, tex(ipxm-r-u48.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u49.pfb) = %{tl_version}, tex(ipxm-r-u4a.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u4b.pfb) = %{tl_version}, tex(ipxm-r-u4c.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u4d.pfb) = %{tl_version}, tex(ipxm-r-u4e.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u4f.pfb) = %{tl_version}, tex(ipxm-r-u50.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u51.pfb) = %{tl_version}, tex(ipxm-r-u52.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u53.pfb) = %{tl_version}, tex(ipxm-r-u54.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u55.pfb) = %{tl_version}, tex(ipxm-r-u56.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u57.pfb) = %{tl_version}, tex(ipxm-r-u58.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u59.pfb) = %{tl_version}, tex(ipxm-r-u5a.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u5b.pfb) = %{tl_version}, tex(ipxm-r-u5c.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u5d.pfb) = %{tl_version}, tex(ipxm-r-u5e.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u5f.pfb) = %{tl_version}, tex(ipxm-r-u60.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u61.pfb) = %{tl_version}, tex(ipxm-r-u62.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u63.pfb) = %{tl_version}, tex(ipxm-r-u64.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u65.pfb) = %{tl_version}, tex(ipxm-r-u66.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u67.pfb) = %{tl_version}, tex(ipxm-r-u68.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u69.pfb) = %{tl_version}, tex(ipxm-r-u6a.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u6b.pfb) = %{tl_version}, tex(ipxm-r-u6c.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u6d.pfb) = %{tl_version}, tex(ipxm-r-u6e.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u6f.pfb) = %{tl_version}, tex(ipxm-r-u70.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u71.pfb) = %{tl_version}, tex(ipxm-r-u72.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u73.pfb) = %{tl_version}, tex(ipxm-r-u74.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u75.pfb) = %{tl_version}, tex(ipxm-r-u76.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u77.pfb) = %{tl_version}, tex(ipxm-r-u78.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u79.pfb) = %{tl_version}, tex(ipxm-r-u7a.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u7b.pfb) = %{tl_version}, tex(ipxm-r-u7c.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u7d.pfb) = %{tl_version}, tex(ipxm-r-u7e.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u7f.pfb) = %{tl_version}, tex(ipxm-r-u80.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u81.pfb) = %{tl_version}, tex(ipxm-r-u82.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u83.pfb) = %{tl_version}, tex(ipxm-r-u84.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u85.pfb) = %{tl_version}, tex(ipxm-r-u86.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u87.pfb) = %{tl_version}, tex(ipxm-r-u88.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u89.pfb) = %{tl_version}, tex(ipxm-r-u8a.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u8b.pfb) = %{tl_version}, tex(ipxm-r-u8c.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u8d.pfb) = %{tl_version}, tex(ipxm-r-u8e.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u8f.pfb) = %{tl_version}, tex(ipxm-r-u90.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u91.pfb) = %{tl_version}, tex(ipxm-r-u92.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u93.pfb) = %{tl_version}, tex(ipxm-r-u94.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u95.pfb) = %{tl_version}, tex(ipxm-r-u96.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u97.pfb) = %{tl_version}, tex(ipxm-r-u98.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u99.pfb) = %{tl_version}, tex(ipxm-r-u9a.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u9b.pfb) = %{tl_version}, tex(ipxm-r-u9c.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u9d.pfb) = %{tl_version}, tex(ipxm-r-u9e.pfb) = %{tl_version}
Provides:       tex(ipxm-r-u9f.pfb) = %{tl_version}, tex(ipxm-r-uf0.pfb) = %{tl_version}
Provides:       tex(ipxm-r-uf8.pfb) = %{tl_version}, tex(ipxm-r-uf9.pfb) = %{tl_version}
Provides:       tex(ipxm-r-ufa.pfb) = %{tl_version}, tex(ipxm-r-ufe.pfb) = %{tl_version}
Provides:       tex(ipxm-r-uff.pfb) = %{tl_version}, tex(c70ipxg.fd) = %{tl_version}
Provides:       tex(c70ipxga.fd) = %{tl_version}, tex(c70ipxm.fd) = %{tl_version}
Provides:       tex(c70ipxma.fd) = %{tl_version}, tex(ot1ipxg.fd) = %{tl_version}
Provides:       tex(ot1ipxm.fd) = %{tl_version}, tex(t1ipxg.fd) = %{tl_version}
Provides:       tex(t1ipxm.fd) = %{tl_version}, tex(ts1ipxg.fd) = %{tl_version}
Provides:       tex(ts1ipxm.fd) = %{tl_version}

%description -n texlive-ipaex-type1
The package contains the IPAex Fonts converted into Unicode
subfonts in Type1 format, which is most suitable for use with
the CJK package. Font conversion was done with ttf2pt1.

%package -n texlive-ipaex-type1-doc
Summary:        Documentation for ipaex-type1
Version:        svn47700
Provides:       tex-ipaex-type1-doc
AutoReqProv:    No

%description -n texlive-ipaex-type1-doc
Documentation for ipaex-type1

%package -n texlive-ifetex
Provides:       tex-ifetex = %{tl_version}
License:        LPPL 1.3
Summary:        Provides \ifetex switch
Version:        svn47231
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(ifetex.sty) = %{tl_version}, tex(ifetex.tex) = %{tl_version}

%description -n texlive-ifetex
The package provides the switch \ifetex which indicates whether
e-TeX is available or not. The package can be loaded as LaTeX
package using \usepackage{ifetex} or in plain TeX using \input
ifetex. In either case it aborts silently if the \ifetex macro
is already defined. The package's test is whether \eTeXversion
is defined as a primitive; if it is, the package assumes e-TeX
features are available.

%package -n texlive-ifetex-doc
Summary:        Documentation for ifetex
Version:        svn47231
Provides:       tex-ifetex-doc
AutoReqProv:    No

%description -n texlive-ifetex-doc
Documentation for ifetex

%package -n texlive-iftex
Provides:       tex-iftex = %{tl_version}
License:        LPPL 1.3
Summary:        Am I running under pdfTeX, XeTeX or LuaTeX?
Version:        svn29654.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(iftex.sty) = %{tl_version}

%description -n texlive-iftex
The package, which works both for Plain TeX and for LaTeX,
defines the \ifPDFTeX, \ifXeTeX, and \ifLuaTeX conditionals for
testing which engine is being used for typesetting. The package
also provides the \RequirePDFTeX, \RequireXeTeX, and
\RequireLuaTeX commands which throw an error if pdfTeX, XeTeX
or LuaTeX (respectively) is not the engine in use.

%package -n texlive-iftex-doc
Summary:        Documentation for iftex
Version:        svn29654.0.2

Provides:       tex-iftex-doc
AutoReqProv:    No

%description -n texlive-iftex-doc
Documentation for iftex

%package -n texlive-insbox
Provides:       tex-insbox = %{tl_version}
License:        Public Domain
Summary:        Insert pictures/boxes into paragraphs
Version:        svn34299.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(insbox.tex) = %{tl_version}

%description -n texlive-insbox
The package provides convenient bundling of the \parshape
primitive. LaTeX users should note that this is a generic
package, and should be loaded using \input .

%package -n texlive-insbox-doc
Summary:        Documentation for insbox
Version:        svn34299.2.2

Provides:       tex-insbox-doc
AutoReqProv:    No

%description -n texlive-insbox-doc
Documentation for insbox

%package -n texlive-hyphen-ethiopic
Provides:       tex-hyphen-ethiopic = %{tl_version}
License:        LPPL
Summary:        Hyphenation patterns for Ethiopic scripts
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-ethiopic
Hyphenation patterns for languages written using the Ethiopic
script for Unicode engines. They are not supposed to be
linguistically relevant in all cases and should, for proper
typography, be replaced by files tailored to individual
languages.

%post -n texlive-hyphen-ethiopic
if [ $1 -gt 0 ] ; then
sed -i '/ethiopic.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "ethiopic loadhyph-mul-ethi.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=amharic/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=amharic" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=geez/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=geez" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{ethiopic}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{ethiopic}{loadhyph-mul-ethi.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{amharic}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{amharic}{loadhyph-mul-ethi.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{geez}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{geez}{loadhyph-mul-ethi.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-ethiopic
if [ $1 == 0 ] ; then
sed -i '/ethiopic.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=amharic/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=geez/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{ethiopic}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{amharic}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{geez}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-arabic
Provides:       tex-hyphen-arabic = %{tl_version}
License:        LPPL
Summary:        (No) Arabic hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-arabic
Prevent hyphenation in Arabic.

%post -n texlive-hyphen-arabic
if [ $1 -gt 0 ] ; then
sed -i '/arabic.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "arabic zerohyph.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{arabic}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{arabic}{zerohyph.tex}{}{}{}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-arabic
if [ $1 == 0 ] ; then
sed -i '/arabic.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{arabic}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-farsi
Provides:       tex-hyphen-farsi = %{tl_version}
License:        LPPL
Summary:        (No) Persian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-farsi
Prevent hyphenation in Persian.

%post -n texlive-hyphen-farsi
if [ $1 -gt 0 ] ; then
sed -i '/farsi.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "farsi zerohyph.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=persian/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=persian" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{farsi}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{farsi}{zerohyph.tex}{}{}{}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{persian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{persian}{zerohyph.tex}{}{}{}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-farsi
if [ $1 == 0 ] ; then
sed -i '/farsi.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=persian/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{farsi}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{persian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-imsproc
Provides:       tex-imsproc = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset IMS conference proceedings
Version:        svn29803.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amstex.sty), tex(amsmath.sty), tex(amsfonts.sty)
Provides:       tex(imsproc.cls) = %{tl_version}

%description -n texlive-imsproc
The class typesets papers for IMS (Iranian Mathematical
Society) conference proceedings. The class uses the XePersian
package.

%package -n texlive-imsproc-doc
Summary:        Documentation for imsproc
Version:        svn29803.0.1

Provides:       tex-imsproc-doc
AutoReqProv:    No

%description -n texlive-imsproc-doc
Documentation for imsproc

%package -n texlive-hyphen-chinese
Provides:       tex-hyphen-chinese = %{tl_version}
License:        LPPL
Summary:        Chinese pinyin hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-chinese
Hyphenation patterns for unaccented transliterated Mandarin
Chinese (pinyin) in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-chinese
if [ $1 -gt 0 ] ; then
sed -i '/pinyin.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "pinyin loadhyph-zh-latn-pinyin.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{pinyin}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{pinyin}{loadhyph-zh-latn-pinyin.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-chinese
if [ $1 == 0 ] ; then
sed -i '/pinyin.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{pinyin}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-impatient-cn-doc
Summary:        Documentation for impatient-cn
Version:        svn35576.0

Provides:       tex-impatient-cn-doc
AutoReqProv:    No

%description -n texlive-impatient-cn-doc
Documentation for impatient-cn

%package -n texlive-hyphen-bulgarian
Provides:       tex-hyphen-bulgarian = %{tl_version}
License:        LPPL
Summary:        Bulgarian hyphenation patterns
Version:        svn48290
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-bulgarian
Hyphenation patterns for Bulgarian in T2A and UTF-8 encodings.

%post -n texlive-hyphen-bulgarian
if [ $1 -gt 0 ] ; then
sed -i '/bulgarian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "bulgarian loadhyph-bg.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{bulgarian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{bulgarian}{loadhyph-bg.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-bulgarian
if [ $1 == 0 ] ; then
sed -i '/bulgarian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{bulgarian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-mongolian
Provides:       tex-hyphen-mongolian = %{tl_version}
License:        LPPL
Summary:        Mongolian hyphenation patterns in Cyrillic script
Version:        svn41113

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-mongolian
Hyphenation patterns for Mongolian in T2A, LMC and UTF-8
encodings. LMC encoding is used in MonTeX. The package includes
two sets of patterns that will hopefully be merged in future.

%post -n texlive-hyphen-mongolian
if [ $1 -gt 0 ] ; then
sed -i '/mongolian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "mongolian loadhyph-mn-cyrl.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{mongolian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{mongolian}{loadhyph-mn-cyrl.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/mongolianlmc.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "mongolianlmc loadhyph-mn-cyrl-x-lmc.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{mongolianlmc}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{mongolianlmc}{loadhyph-mn-cyrl-x-lmc.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-mongolian
if [ $1 == 0 ] ; then
sed -i '/mongolian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{mongolian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/mongolianlmc.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{mongolianlmc}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-russian
Provides:       tex-hyphen-russian = %{tl_version}
License:        LPPL
Summary:        Russian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8, tex-ruhyphen

%description -n texlive-hyphen-russian
Hyphenation patterns for Russian in T2A and UTF-8 encodings.
For 8-bit engines, the 'ruhyphen' package provides a number of
different pattern sets, as well as different (8-bit) encodings,
that can be chosen at format-generation time.  The UTF-8
version only provides the default pattern set.  A mechanism
similar to the one used for 8-bit patterns may be implemented
in the future.

%post -n texlive-hyphen-russian
if [ $1 -gt 0 ] ; then
sed -i '/russian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "russian loadhyph-ru.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{russian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{russian}{loadhyph-ru.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-russian
if [ $1 == 0 ] ; then
sed -i '/russian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{russian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-serbian
Provides:       tex-hyphen-serbian = %{tl_version}
License:        GPL+
Summary:        Serbian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-serbian
Hyphenation patterns for Serbian in T1/EC, T2A and UTF-8
encodings. For 8-bit engines the patterns are available
separately as 'serbian' in T1/EC encoding for Latin script and
'serbianc' in T2A encoding for Cyrillic script. Unicode engines
should only use 'serbian' which has patterns in both scripts
combined.

%post -n texlive-hyphen-serbian
if [ $1 -gt 0 ] ; then
sed -i '/serbian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "serbian loadhyph-sr-latn.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{serbian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{serbian}{loadhyph-sr-latn.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/serbianc.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "serbianc loadhyph-sr-cyrl.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{serbianc}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{serbianc}{loadhyph-sr-cyrl.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-serbian
if [ $1 == 0 ] ; then
sed -i '/serbian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{serbian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/serbianc.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{serbianc}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-ukrainian
Provides:       tex-hyphen-ukrainian = %{tl_version}
License:        LPPL
Summary:        Ukrainian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8, tex-ukrhyph

%description -n texlive-hyphen-ukrainian
Hyphenation patterns for Ukrainian in T2A and UTF-8 encodings.
For 8-bit engines, the 'ukrhyph' package provides a number of
different pattern sets, as well as different (8-bit) encodings,
that can be chosen at format-generation time.  The UTF-8
version only provides the default pattern set.  A mechanism
similar to the one used for 8-bit patterns may be implemented
in the future.

%post -n texlive-hyphen-ukrainian
if [ $1 -gt 0 ] ; then
sed -i '/ukrainian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "ukrainian loadhyph-uk.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{ukrainian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{ukrainian}{loadhyph-uk.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-ukrainian
if [ $1 == 0 ] ; then
sed -i '/ukrainian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{ukrainian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-czech
Provides:       tex-hyphen-czech = %{tl_version}
License:        LPPL
Summary:        Czech hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-czech
Hyphenation patterns for Czech in T1/EC and UTF-8 encodings.
Original patterns 'czhyphen' are still distributed in the
'csplain' package and loaded with ISO Latin 2 encoding (IL2).

%post -n texlive-hyphen-czech
if [ $1 -gt 0 ] ; then
sed -i '/czech.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "czech loadhyph-cs.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{czech}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{czech}{loadhyph-cs.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-czech
if [ $1 == 0 ] ; then
sed -i '/czech.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{czech}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-slovak
Provides:       tex-hyphen-slovak = %{tl_version}
License:        LPPL
Summary:        Slovak hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-slovak
Hyphenation patterns for Slovak in T1/EC and UTF-8 encodings.
Original patterns 'skhyphen' are still distributed in the
'csplain' package and loaded with ISO Latin 2 encoding (IL2).

%post -n texlive-hyphen-slovak
if [ $1 -gt 0 ] ; then
sed -i '/slovak.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "slovak loadhyph-sk.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{slovak}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{slovak}{loadhyph-sk.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-slovak
if [ $1 == 0 ] ; then
sed -i '/slovak.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{slovak}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-english
Provides:       tex-hyphen-english = %{tl_version}
License:        LPPL
Summary:        English hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-english
Additional hyphenation patterns for American and British
English in ASCII encoding.  The American English patterns
(usenglishmax) greatly extend the standard patterns from Knuth
to find many additional hyphenation points.  British English
hyphenation is completely different from US English, so has its
own set of patterns.

%post -n texlive-hyphen-english
if [ $1 -gt 0 ] ; then
sed -i '/ukenglish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "ukenglish loadhyph-en-gb.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=british/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=british" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=UKenglish/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=UKenglish" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{ukenglish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{ukenglish}{loadhyph-en-gb.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{british}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{british}{loadhyph-en-gb.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{UKenglish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{UKenglish}{loadhyph-en-gb.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/usenglishmax.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "usenglishmax loadhyph-en-us.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{usenglishmax}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{usenglishmax}{loadhyph-en-us.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-english
if [ $1 == 0 ] ; then
sed -i '/ukenglish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=british/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=UKenglish/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{ukenglish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{british}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{UKenglish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/usenglishmax.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{usenglishmax}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-impatient-doc
Summary:        Documentation for impatient
Version:        svn35573.0

Provides:       tex-impatient-doc
AutoReqProv:    No

%description -n texlive-impatient-doc
Documentation for impatient

%package -n texlive-intro-scientific-doc
Summary:        Documentation for intro-scientific
Version:        svn15878.5th_edition

Provides:       tex-intro-scientific-doc
AutoReqProv:    No

%description -n texlive-intro-scientific-doc
Documentation for intro-scientific

%package -n texlive-hyphen-armenian
Provides:       tex-hyphen-armenian = %{tl_version}
License:        LPPL
Summary:        Armenian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-armenian
Hyphenation patterns for Armenian for Unicode engines.

%post -n texlive-hyphen-armenian
if [ $1 -gt 0 ] ; then
sed -i '/armenian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "armenian loadhyph-hy.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{armenian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{armenian}{loadhyph-hy.tex}{}{1}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-armenian
if [ $1 == 0 ] ; then
sed -i '/armenian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{armenian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-croatian
Provides:       tex-hyphen-croatian = %{tl_version}
License:        LPPL 1.3
Summary:        Croatian hyphenation patterns
Version:        svn41113

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-croatian
Hyphenation patterns for Croatian in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-croatian
if [ $1 -gt 0 ] ; then
sed -i '/croatian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "croatian loadhyph-hr.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{croatian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{croatian}{loadhyph-hr.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-croatian
if [ $1 == 0 ] ; then
sed -i '/croatian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{croatian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-danish
Provides:       tex-hyphen-danish = %{tl_version}
License:        LPPL
Summary:        Danish hyphenation patterns
Version:        svn41113

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-danish
Hyphenation patterns for Danish in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-danish
if [ $1 -gt 0 ] ; then
sed -i '/danish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "danish loadhyph-da.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{danish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{danish}{loadhyph-da.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-danish
if [ $1 == 0 ] ; then
sed -i '/danish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{danish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-dutch
Provides:       tex-hyphen-dutch = %{tl_version}
License:        LPPL
Summary:        Dutch hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-dutch
Hyphenation patterns for Dutch in T1/EC and UTF-8 encodings.
These patterns don't handle cases like 'menuutje' > 'menu-tje',
and don't hyphenate words that have different hyphenations
according to their meaning.

%post -n texlive-hyphen-dutch
if [ $1 -gt 0 ] ; then
sed -i '/dutch.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "dutch loadhyph-nl.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{dutch}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{dutch}{loadhyph-nl.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-dutch
if [ $1 == 0 ] ; then
sed -i '/dutch.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{dutch}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-estonian
Provides:       tex-hyphen-estonian = %{tl_version}
License:        LPPL
Summary:        Estonian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-estonian
Hyphenation patterns for Estonian in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-estonian
if [ $1 -gt 0 ] ; then
sed -i '/estonian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "estonian loadhyph-et.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{estonian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{estonian}{loadhyph-et.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-estonian
if [ $1 == 0 ] ; then
sed -i '/estonian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{estonian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-finnish
Provides:       tex-hyphen-finnish = %{tl_version}
License:        Public Domain
Summary:        Finnish hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-finnish
Hyphenation patterns for Finnish in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-finnish
if [ $1 -gt 0 ] ; then
sed -i '/finnish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "finnish loadhyph-fi.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{finnish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{finnish}{loadhyph-fi.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-finnish
if [ $1 == 0 ] ; then
sed -i '/finnish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{finnish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-friulan
Provides:       tex-hyphen-friulan = %{tl_version}
License:        LPPL
Summary:        Friulan hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-friulan
Hyphenation patterns for Friulan in ASCII encoding. They are
supposed to comply with the common spelling of the Friulan
(Furlan) language as fixed by the Regional Law N.15/96 dated
November 6, 1996 and its following amendments.

%post -n texlive-hyphen-friulan
if [ $1 -gt 0 ] ; then
sed -i '/friulan.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "friulan loadhyph-fur.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{friulan}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{friulan}{loadhyph-fur.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-friulan
if [ $1 == 0 ] ; then
sed -i '/friulan.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{friulan}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-hungarian
Provides:       tex-hyphen-hungarian = %{tl_version}
License:        GPL+
Summary:        Hungarian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-hungarian
Hyphenation patterns for Hungarian in T1/EC and UTF-8
encodings. From https://github.com/nagybence/huhyphn/.

%post -n texlive-hyphen-hungarian
if [ $1 -gt 0 ] ; then
sed -i '/hungarian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "hungarian loadhyph-hu.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{hungarian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{hungarian}{loadhyph-hu.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-hungarian
if [ $1 == 0 ] ; then
sed -i '/hungarian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{hungarian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-hungarian-doc
Summary:        Documentation for hyphen-hungarian
Version:        svn40340

Provides:       tex-hyphen-hungarian-doc
AutoReqProv:    No
Requires:       tex-hyph-utf8-doc

%description -n texlive-hyphen-hungarian-doc
Documentation for hyphen-hungarian

%package -n texlive-hyphen-icelandic
Provides:       tex-hyphen-icelandic = %{tl_version}
License:        LPPL
Summary:        Icelandic hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-icelandic
Hyphenation patterns for Icelandic in T1/EC and UTF-8
encodings.

%post -n texlive-hyphen-icelandic
if [ $1 -gt 0 ] ; then
sed -i '/icelandic.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "icelandic loadhyph-is.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{icelandic}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{icelandic}{loadhyph-is.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-icelandic
if [ $1 == 0 ] ; then
sed -i '/icelandic.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{icelandic}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-irish
Provides:       tex-hyphen-irish = %{tl_version}
License:        LPPL
Summary:        Irish hyphenation patterns
Version:        svn41113

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-irish
Hyphenation patterns for Irish (Gaeilge) in T1/EC and UTF-8
encodings. Visit http://borel.slu.edu/fleiscin/index.html for
more information.

%post -n texlive-hyphen-irish
if [ $1 -gt 0 ] ; then
sed -i '/irish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "irish loadhyph-ga.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{irish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{irish}{loadhyph-ga.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-irish
if [ $1 == 0 ] ; then
sed -i '/irish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{irish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-kurmanji
Provides:       tex-hyphen-kurmanji = %{tl_version}
License:        LPPL
Summary:        Kurmanji hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-kurmanji
Hyphenation patterns for Kurmanji (Northern Kurdish) as spoken
in Turkey and by the Kurdish diaspora in Europe, in T1/EC and
UTF-8 encodings.

%post -n texlive-hyphen-kurmanji
if [ $1 -gt 0 ] ; then
sed -i '/kurmanji.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "kurmanji loadhyph-kmr.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{kurmanji}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{kurmanji}{loadhyph-kmr.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-kurmanji
if [ $1 == 0 ] ; then
sed -i '/kurmanji.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{kurmanji}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-latin
Provides:       tex-hyphen-latin = %{tl_version}
License:        LPPL
Summary:        Latin and classical Latin hyphenation patterns
Version:        svn47375
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-latin
Hyphenation patterns for Latin in T1/EC and UTF-8 encodings,
mainly in modern spelling (u when u is needed and v when v is
needed), medieval spelling with the ligatures \ae and \oe and
the (uncial) lowercase 'v' written as a 'u' is also supported.
Apparently there is no conflict between the patterns of modern
Latin and those of medieval Latin. Hyphenation patterns for the
Classical Latin in T1/EC and UTF-8 encodings. Classical Latin
hyphenation patterns are different from those of 'plain' Latin,
the latter being more adapted to modern Latin.

%post -n texlive-hyphen-latin
if [ $1 -gt 0 ] ; then
sed -i '/latin.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "latin loadhyph-la.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{latin}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{latin}{loadhyph-la.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/classiclatin.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "classiclatin loadhyph-la-x-classic.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{classiclatin}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{classiclatin}{loadhyph-la-x-classic.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-latin
if [ $1 == 0 ] ; then
sed -i '/latin.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{latin}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/classiclatin.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{classiclatin}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-latvian
Provides:       tex-hyphen-latvian = %{tl_version}
License:        LPPL
Summary:        Latvian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-latvian
Hyphenation patterns for Latvian in L7X and UTF-8 encodings.

%post -n texlive-hyphen-latvian
if [ $1 -gt 0 ] ; then
sed -i '/latvian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "latvian loadhyph-lv.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{latvian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{latvian}{loadhyph-lv.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-latvian
if [ $1 == 0 ] ; then
sed -i '/latvian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{latvian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-lithuanian
Provides:       tex-hyphen-lithuanian = %{tl_version}
License:        LPPL
Summary:        Lithuanian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-lithuanian
Hyphenation patterns for Lithuanian in L7X and UTF-8 encodings.
\lefthyphenmin and \righthyphenmin have to be at least 2.

%post -n texlive-hyphen-lithuanian
if [ $1 -gt 0 ] ; then
sed -i '/lithuanian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "lithuanian loadhyph-lt.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{lithuanian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{lithuanian}{loadhyph-lt.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-lithuanian
if [ $1 == 0 ] ; then
sed -i '/lithuanian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{lithuanian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-norwegian
Provides:       tex-hyphen-norwegian = %{tl_version}
License:        LPPL
Summary:        Norwegian Bokmal and Nynorsk hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-norwegian
Hyphenation patterns for Norwegian Bokmal and Nynorsk in T1/EC
and UTF-8 encodings.

%post -n texlive-hyphen-norwegian
if [ $1 -gt 0 ] ; then
sed -i '/bokmal.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "bokmal loadhyph-nb.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=norwegian/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=norwegian" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=norsk/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=norsk" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{bokmal}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{bokmal}{loadhyph-nb.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{norwegian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{norwegian}{loadhyph-nb.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{norsk}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{norsk}{loadhyph-nb.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/nynorsk.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "nynorsk loadhyph-nn.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{nynorsk}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{nynorsk}{loadhyph-nn.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-norwegian
if [ $1 == 0 ] ; then
sed -i '/bokmal.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=norwegian/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=norsk/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{bokmal}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{norwegian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{norsk}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/nynorsk.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{nynorsk}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-piedmontese
Provides:       tex-hyphen-piedmontese = %{tl_version}
License:        LPPL
Summary:        Piedmontese hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-piedmontese
Hyphenation patterns for Piedmontese in ASCII encoding.
Compliant with 'Gramatica dla lengua piemonteisa' by Camillo
Brero.

%post -n texlive-hyphen-piedmontese
if [ $1 -gt 0 ] ; then
sed -i '/piedmontese.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "piedmontese loadhyph-pms.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{piedmontese}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{piedmontese}{loadhyph-pms.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-piedmontese
if [ $1 == 0 ] ; then
sed -i '/piedmontese.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{piedmontese}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-romanian
Provides:       tex-hyphen-romanian = %{tl_version}
License:        LPPL
Summary:        Romanian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-romanian
Hyphenation patterns for Romanian in T1/EC and UTF-8 encodings.
The UTF-8 patterns use U+0219 for the character 's with comma
accent' and U+021B for 't with comma accent', but we may
consider using U+015F and U+0163 as well in the future.

%post -n texlive-hyphen-romanian
if [ $1 -gt 0 ] ; then
sed -i '/romanian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "romanian loadhyph-ro.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{romanian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{romanian}{loadhyph-ro.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-romanian
if [ $1 == 0 ] ; then
sed -i '/romanian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{romanian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-romansh
Provides:       tex-hyphen-romansh = %{tl_version}
License:        LPPL
Summary:        Romansh hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-romansh
Hyphenation patterns for Romansh in ASCII encoding. They are
supposed to comply with the rules indicated by the Lia
Rumantscha (Romansh language society).

%post -n texlive-hyphen-romansh
if [ $1 -gt 0 ] ; then
sed -i '/romansh.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "romansh loadhyph-rm.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{romansh}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{romansh}{loadhyph-rm.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-romansh
if [ $1 == 0 ] ; then
sed -i '/romansh.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{romansh}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-slovenian
Provides:       tex-hyphen-slovenian = %{tl_version}
License:        LPPL
Summary:        Slovenian hyphenation patterns
Version:        svn41113

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-slovenian
Hyphenation patterns for Slovenian in T1/EC and UTF-8
encodings.

%post -n texlive-hyphen-slovenian
if [ $1 -gt 0 ] ; then
sed -i '/slovenian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "slovenian loadhyph-sl.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=slovene/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=slovene" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{slovenian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{slovenian}{loadhyph-sl.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{slovene}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{slovene}{loadhyph-sl.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-slovenian
if [ $1 == 0 ] ; then
sed -i '/slovenian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=slovene/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{slovenian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{slovene}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-swedish
Provides:       tex-hyphen-swedish = %{tl_version}
License:        LPPL
Summary:        Swedish hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-swedish
Hyphenation patterns for Swedish in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-swedish
if [ $1 -gt 0 ] ; then
sed -i '/swedish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "swedish loadhyph-sv.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{swedish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{swedish}{loadhyph-sv.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-swedish
if [ $1 == 0 ] ; then
sed -i '/swedish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{swedish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-turkish
Provides:       tex-hyphen-turkish = %{tl_version}
License:        Copyright only
Summary:        Turkish hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-turkish
Hyphenation patterns for Turkish in T1/EC and UTF-8 encodings.
The patterns for Turkish were first produced for the Ottoman
Texts Project in 1987 and were suitable for both Modern Turkish
and Ottoman Turkish in Latin script, however the required
character set didn't fit into EC encoding, so support for
Ottoman Turkish had to be dropped to keep compatibility with 8-
bit engines.

%post -n texlive-hyphen-turkish
if [ $1 -gt 0 ] ; then
sed -i '/turkish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "turkish loadhyph-tr.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{turkish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{turkish}{loadhyph-tr.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-turkish
if [ $1 == 0 ] ; then
sed -i '/turkish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{turkish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-uppersorbian
Provides:       tex-hyphen-uppersorbian = %{tl_version}
License:        LPPL
Summary:        Upper Sorbian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-uppersorbian
Hyphenation patterns for Upper Sorbian in T1/EC and UTF-8
encodings.

%post -n texlive-hyphen-uppersorbian
if [ $1 -gt 0 ] ; then
sed -i '/uppersorbian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "uppersorbian loadhyph-hsb.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{uppersorbian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{uppersorbian}{loadhyph-hsb.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-uppersorbian
if [ $1 == 0 ] ; then
sed -i '/uppersorbian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{uppersorbian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-welsh
Provides:       tex-hyphen-welsh = %{tl_version}
License:        LPPL
Summary:        Welsh hyphenation patterns
Version:        svn41113

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-welsh
Hyphenation patterns for Welsh in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-welsh
if [ $1 -gt 0 ] ; then
sed -i '/welsh.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "welsh loadhyph-cy.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{welsh}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{welsh}{loadhyph-cy.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-welsh
if [ $1 == 0 ] ; then
sed -i '/welsh.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{welsh}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-lithuanian
Provides:       tex-lithuanian = %{tl_version}
License:        LPPL
Summary:        Lithuanian language support
Version:        svn46039
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       tex(latin7x.enc) = %{tl_version}, tex(l7x-urwvn.map) = %{tl_version}
Provides:       tex(l7x-uagd.tfm) = %{tl_version}, tex(l7x-uagdo.tfm) = %{tl_version}
Provides:       tex(l7x-uagk.tfm) = %{tl_version}, tex(l7x-uagko.tfm) = %{tl_version}
Provides:       tex(l7x-ubkd.tfm) = %{tl_version}, tex(l7x-ubkdi.tfm) = %{tl_version}
Provides:       tex(l7x-ubkl.tfm) = %{tl_version}, tex(l7x-ubkli.tfm) = %{tl_version}
Provides:       tex(l7x-ucrb.tfm) = %{tl_version}, tex(l7x-ucrbo.tfm) = %{tl_version}
Provides:       tex(l7x-ucrr.tfm) = %{tl_version}, tex(l7x-ucrro.tfm) = %{tl_version}
Provides:       tex(l7x-uhvb.tfm) = %{tl_version}, tex(l7x-uhvbc.tfm) = %{tl_version}
Provides:       tex(l7x-uhvbo.tfm) = %{tl_version}, tex(l7x-uhvboc.tfm) = %{tl_version}
Provides:       tex(l7x-uhvr.tfm) = %{tl_version}, tex(l7x-uhvrc.tfm) = %{tl_version}
Provides:       tex(l7x-uhvro.tfm) = %{tl_version}, tex(l7x-uhvroc.tfm) = %{tl_version}
Provides:       tex(l7x-uncb.tfm) = %{tl_version}, tex(l7x-uncbi.tfm) = %{tl_version}
Provides:       tex(l7x-uncr.tfm) = %{tl_version}, tex(l7x-uncri.tfm) = %{tl_version}
Provides:       tex(l7x-uplb.tfm) = %{tl_version}, tex(l7x-uplbi.tfm) = %{tl_version}
Provides:       tex(l7x-uplr.tfm) = %{tl_version}, tex(l7x-uplri.tfm) = %{tl_version}
Provides:       tex(l7x-utmb.tfm) = %{tl_version}, tex(l7x-utmbi.tfm) = %{tl_version}
Provides:       tex(l7x-utmr.tfm) = %{tl_version}, tex(l7x-utmri.tfm) = %{tl_version}
Provides:       tex(l7x-uzcmi.tfm) = %{tl_version}, tex(cp772.def) = %{tl_version}
Provides:       tex(cp774.def) = %{tl_version}, tex(cp775.def) = %{tl_version}
Provides:       tex(cpKBL.def) = %{tl_version}, tex(cpRIM.def) = %{tl_version}
Provides:       tex(l7xenc.def) = %{tl_version}, tex(l7xenc.sty) = %{tl_version}
Provides:       tex(l7xuag.fd) = %{tl_version}, tex(l7xubk.fd) = %{tl_version}
Provides:       tex(l7xucr.fd) = %{tl_version}, tex(l7xuhv.fd) = %{tl_version}
Provides:       tex(l7xunc.fd) = %{tl_version}, tex(l7xupl.fd) = %{tl_version}
Provides:       tex(l7xutm.fd) = %{tl_version}, tex(l7xuzc.fd) = %{tl_version}
Provides:       tex(latin7.def) = %{tl_version}, tex(lithuanian.ldf) = %{tl_version}
Provides:       tex(lithuanian.sty) = %{tl_version}

%description -n texlive-lithuanian
This language support package provides: Lithuanian language
hyphenation patterns; Lithuanian support for Babel; Lithuanian
mapping and metrics for using the URW base-35 Type 1 fonts;
examples for making Lithuanian fonts with fontinst; and extra
tools for intputenc and fontinst.

%package -n texlive-lithuanian-doc
Summary:        Documentation for lithuanian
Version:        svn46039
Provides:       tex-lithuanian-doc
AutoReqProv:    No

%description -n texlive-lithuanian-doc
Documentation for lithuanian

%package -n texlive-lshort-dutch-doc
Summary:        Documentation for lshort-dutch
Version:        svn15878.1.3

Provides:       tex-lshort-dutch-doc
AutoReqProv:    No

%description -n texlive-lshort-dutch-doc
Documentation for lshort-dutch

%package -n texlive-lshort-finnish-doc
Summary:        Documentation for lshort-finnish
Version:        svn15878.0

Provides:       tex-lshort-finnish-doc
AutoReqProv:    No

%description -n texlive-lshort-finnish-doc
Documentation for lshort-finnish

%package -n texlive-lshort-slovenian-doc
Summary:        Documentation for lshort-slovenian
Version:        svn15878.4.20

Provides:       tex-lshort-slovenian-doc
AutoReqProv:    No

%description -n texlive-lshort-slovenian-doc
Documentation for lshort-slovenian

%package -n texlive-lshort-turkish-doc
Summary:        Documentation for lshort-turkish
Version:        svn15878.4.20

Provides:       tex-lshort-turkish-doc
AutoReqProv:    No

%description -n texlive-lshort-turkish-doc
Documentation for lshort-turkish

%package -n texlive-nevelok
Provides:       tex-nevelok = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX package for automatic definite articles for Hungarian
Version:        svn39029

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xstring.sty)
Provides:       tex(nevelok.sty) = %{tl_version}

%description -n texlive-nevelok
LaTeX package for automatic definite articles for Hungarian

%package -n texlive-nevelok-doc
Summary:        Documentation for nevelok
Version:        svn39029

Provides:       tex-nevelok-doc
AutoReqProv:    No

%description -n texlive-nevelok-doc
Documentation for nevelok

%package -n texlive-swebib
Provides:       tex-swebib = %{tl_version}
License:        LPPL 1.2
Summary:        Swedish bibliography styles
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-swebib
The bundle contains Swedish versions of the standard
bibliography styles, and of the style plainnat. The styles
should be funtionally equivalent to the corresponding original
styles, apart from the Swedish translations. The styles do not
implement Swedish collation.

%package -n texlive-swebib-doc
Summary:        Documentation for swebib
Version:        svn15878.0

Provides:       tex-swebib-doc
AutoReqProv:    No

%description -n texlive-swebib-doc
Documentation for swebib

%package -n texlive-turkmen
Provides:       tex-turkmen = %{tl_version}
License:        LPPL
Summary:        Babel support for Turkmen
Version:        svn17748.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(turkmen.ldf) = %{tl_version}

%description -n texlive-turkmen
The package provides support for Turkmen in babel, but
integration with babel is not available.

%package -n texlive-turkmen-doc
Summary:        Documentation for turkmen
Version:        svn17748.0.2

Provides:       tex-turkmen-doc
AutoReqProv:    No

%description -n texlive-turkmen-doc
Documentation for turkmen

%package -n texlive-hyphen-basque
Provides:       tex-hyphen-basque = %{tl_version}
License:        Bahyph
Summary:        Basque hyphenation patterns
Version:        svn41113

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-basque
Hyphenation patterns for Basque in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-basque
if [ $1 -gt 0 ] ; then
sed -i '/basque.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "basque loadhyph-eu.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{basque}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{basque}{loadhyph-eu.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-basque
if [ $1 == 0 ] ; then
sed -i '/basque.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{basque}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-french
Provides:       tex-hyphen-french = %{tl_version}
License:        LPPL
Summary:        French hyphenation patterns
Version:        svn41113

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-french
Hyphenation patterns for French in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-french
if [ $1 -gt 0 ] ; then
sed -i '/french.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "french loadhyph-fr.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=patois/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=patois" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=francais/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=francais" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{french}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{french}{loadhyph-fr.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{patois}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{patois}{loadhyph-fr.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{francais}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{francais}{loadhyph-fr.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-french
if [ $1 == 0 ] ; then
sed -i '/french.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=patois/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=francais/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{french}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{patois}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{francais}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-impatient-fr-doc
Summary:        Documentation for impatient-fr
Version:        svn15878.0

Provides:       tex-impatient-fr-doc
AutoReqProv:    No

%description -n texlive-impatient-fr-doc
Documentation for impatient-fr

%package -n texlive-impnattypo
Provides:       tex-impnattypo = %{tl_version}
License:        LPPL 1.3
Summary:        Support typography of l'Imprimerie Nationale Francaise
Version:        svn36448.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty), tex(kvoptions.sty), tex(xcolor.sty), tex(luatexbase.sty)
Requires:       tex(luacode.sty)
Provides:       tex(impnattypo.sty) = %{tl_version}

%description -n texlive-impnattypo
The package provides useful macros implementing recommendations
by the French Imprimerie Nationale.

%package -n texlive-impnattypo-doc
Summary:        Documentation for impnattypo
Version:        svn36448.1.4

Provides:       tex-impnattypo-doc
AutoReqProv:    No

%description -n texlive-impnattypo-doc
Documentation for impnattypo

%package -n texlive-hyphen-german
Provides:       tex-hyphen-german = %{tl_version}
License:        LPPL
Summary:        German hyphenation patterns
Version:        svn47375
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8
Provides:       tex(dehyphn.tex) = %{tl_version}, tex(dehypht.tex) = %{tl_version}
Provides:       tex(dehyphtex.tex) = %{tl_version}

%description -n texlive-hyphen-german
Hyphenation patterns for German in T1/EC and UTF-8 encodings,
for traditional and reformed spelling, including Swiss German.
The package includes the latest patterns from dehyph-exptl
(known to TeX under names 'german', 'ngerman' and
'swissgerman'), however 8-bit engines still load old versions
of patterns for 'german' and 'ngerman' for backward-
compatibility reasons. Swiss German patterns are suitable for
Swiss Standard German (Hochdeutsch) not the Alemannic dialects
spoken in Switzerland (Schwyzerduetsch). There are no known
patterns for written Schwyzerduetsch.

%post -n texlive-hyphen-german
if [ $1 -gt 0 ] ; then
sed -i '/german.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "german loadhyph-de-1901.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{german}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{german}{loadhyph-de-1901.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/ngerman.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "ngerman loadhyph-de-1996.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{ngerman}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{ngerman}{loadhyph-de-1996.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/swissgerman.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "swissgerman loadhyph-de-ch-1901.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{swissgerman}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{swissgerman}{loadhyph-de-ch-1901.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-german
if [ $1 == 0 ] ; then
sed -i '/german.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{german}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/ngerman.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{ngerman}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/swissgerman.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{swissgerman}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-greek
Provides:       tex-hyphen-greek = %{tl_version}
License:        LPPL
Summary:        Modern Greek hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8
Provides:       tex(grmhyph5.tex) = %{tl_version}, tex(grphyph5.tex) = %{tl_version}

%description -n texlive-hyphen-greek
Hyphenation patterns for Modern Greek in monotonic and
polytonic spelling in LGR and UTF-8 encodings.  Patterns in UTF-
8 use two code positions for each of the vowels with acute
accent (a.k.a tonos, oxia), e.g., U+03AC, U+1F71 for alpha.

%post -n texlive-hyphen-greek
if [ $1 -gt 0 ] ; then
sed -i '/monogreek.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "monogreek loadhyph-el-monoton.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{monogreek}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{monogreek}{loadhyph-el-monoton.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/greek.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "greek loadhyph-el-polyton.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=polygreek/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=polygreek" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{greek}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{greek}{loadhyph-el-polyton.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{polygreek}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{polygreek}{loadhyph-el-polyton.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-greek
if [ $1 == 0 ] ; then
sed -i '/monogreek.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{monogreek}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/greek.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=polygreek/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{greek}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{polygreek}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-greek-doc
Summary:        Documentation for hyphen-greek
Version:        svn40340

Provides:       tex-hyphen-greek-doc
AutoReqProv:    No
Requires:       tex-hyph-utf8-doc

%description -n texlive-hyphen-greek-doc
Documentation for hyphen-greek

%package -n texlive-hyphen-ancientgreek
Provides:       tex-hyphen-ancientgreek = %{tl_version}
License:        LPPL
Summary:        Ancient Greek hyphenation patterns
Version:        svn41189

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8
Provides:       tex(grahyph5.tex) = %{tl_version}, tex(ibyhyph.tex) = %{tl_version}

%description -n texlive-hyphen-ancientgreek
Hyphenation patterns for Ancient Greek in LGR and UTF-8
encodings, including support for (obsolete) Ibycus font
encoding. Patterns in UTF-8 use two code positions for each of
the vowels with acute accent (a.k.a tonos, oxia), e.g., U+03AE,
U+1F75 for eta.

%post -n texlive-hyphen-ancientgreek
if [ $1 -gt 0 ] ; then
sed -i '/ancientgreek.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "ancientgreek loadhyph-grc.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{ancientgreek}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{ancientgreek}{loadhyph-grc.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/ibycus.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "ibycus ibyhyph.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{ibycus}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{ibycus}{ibyhyph.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-ancientgreek
if [ $1 == 0 ] ; then
sed -i '/ancientgreek.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{ancientgreek}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/ibycus.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{ibycus}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-ibycus-babel
Provides:       tex-ibycus-babel = %{tl_version}
License:        LPPL
Summary:        Use the Ibycus 4 Greek font with Babel
Version:        svn15878.3.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ibycus.ldf) = %{tl_version}, tex(lgienc.def) = %{tl_version}
Provides:       tex(lgifib.fd) = %{tl_version}

%description -n texlive-ibycus-babel
The package allows you to use the Ibycus 4 font for ancient
Greek with Babel. It uses a Perl script to generate hyphenation
patterns for Ibycus from those for the ordinary Babel encoding,
cbgreek. It sets up ibycus as a pseudo-language you can specify
in the normal Babel manner. For proper hyphenation of Greek
quoted in mid-paragraph, you should use it with elatex (all
current distributions of LaTeX are built with e-TeX, so the
constraint should not be onerous).

%package -n texlive-ibycus-babel-doc
Summary:        Documentation for ibycus-babel
Version:        svn15878.3.0

Provides:       tex-ibycus-babel-doc
AutoReqProv:    No

%description -n texlive-ibycus-babel-doc
Documentation for ibycus-babel

%package -n texlive-ibygrk
Provides:       tex-ibygrk = %{tl_version}
License:        GPL+
Summary:        Fonts and macros to typeset ancient Greek
Version:        svn15878.4.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(IbycusHTG.enc) = %{tl_version}, tex(iby.map) = %{tl_version}
Provides:       tex(ibycus4.map) = %{tl_version}, tex(fibb84.tfm) = %{tl_version}
Provides:       tex(fibb848.tfm) = %{tl_version}, tex(fibb849.tfm) = %{tl_version}
Provides:       tex(fibo84.tfm) = %{tl_version}, tex(fibo848.tfm) = %{tl_version}
Provides:       tex(fibo849.tfm) = %{tl_version}, tex(fibr84.tfm) = %{tl_version}
Provides:       tex(fibr848.tfm) = %{tl_version}, tex(fibr849.tfm) = %{tl_version}
Provides:       tex(fibb84.pfb) = %{tl_version}, tex(fibr84.pfb) = %{tl_version}
Provides:       tex(Uibycus.fd) = %{tl_version}, tex(Uibycus4.fd) = %{tl_version}
Provides:       tex(iby4extr.tex) = %{tl_version}, tex(ibycus4.map) = %{tl_version}
Provides:       tex(ibycus4.sty) = %{tl_version}, tex(ibycus4.tex) = %{tl_version}
Provides:       tex(ibycusps.tex) = %{tl_version}, tex(psibycus.sty) = %{tl_version}
Provides:       tex(pssetiby.tex) = %{tl_version}, tex(setiby4.tex) = %{tl_version}
Provides:       tex(tlgsqq.tex) = %{tl_version}, tex(version4.tex) = %{tl_version}

%description -n texlive-ibygrk
Ibycus is a Greek typeface, based on Silvio Levy's realisation
of a classic Didot cut of Greek type from around 1800. The
fonts are available both as Metafont source and in Adobe Type 1
format. This distribution of ibycus is accompanied by a set of
macro packages to use it with Plain TeX or LaTeX, but for use
with Babel, see the ibycus-babel package.

%package -n texlive-ibygrk-doc
Summary:        Documentation for ibygrk
Version:        svn15878.4.5

Provides:       tex-ibygrk-doc
AutoReqProv:    No

%description -n texlive-ibygrk-doc
Documentation for ibygrk


%package -n texlive-hyphen-indic
Provides:       tex-hyphen-indic = %{tl_version}
License:        LPPL
Summary:        Indic hyphenation patterns
Version:        svn48297
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-indic
Hyphenation patterns for Assamese, Bengali, Gujarati, Hindi,
Kannada, Malayalam, Marathi, Odia, Panjabi, Tamil and Telugu
for Unicode engines.

%post -n texlive-hyphen-indic
if [ $1 -gt 0 ] ; then
sed -i '/assamese.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "assamese loadhyph-as.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{assamese}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{assamese}{loadhyph-as.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/bengali.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "bengali loadhyph-bn.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{bengali}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{bengali}{loadhyph-bn.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/gujarati.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "gujarati loadhyph-gu.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{gujarati}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{gujarati}{loadhyph-gu.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/hindi.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "hindi loadhyph-hi.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{hindi}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{hindi}{loadhyph-hi.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/kannada.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "kannada loadhyph-kn.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{kannada}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{kannada}{loadhyph-kn.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/malayalam.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "malayalam loadhyph-ml.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{malayalam}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{malayalam}{loadhyph-ml.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/marathi.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "marathi loadhyph-mr.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{marathi}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{marathi}{loadhyph-mr.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/oriya.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "oriya loadhyph-or.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{oriya}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{oriya}{loadhyph-or.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/odia.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "odia loadhyph-or.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{odia}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{odia}{loadhyph-or.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/panjabi.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "panjabi loadhyph-pa.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{panjabi}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{panjabi}{loadhyph-pa.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/tamil.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "tamil loadhyph-ta.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{tamil}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{tamil}{loadhyph-ta.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/telugu.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "telugu loadhyph-te.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{telugu}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{telugu}{loadhyph-te.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-indic
if [ $1 == 0 ] ; then
sed -i '/assamese.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{assamese}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/bengali.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{bengali}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/gujarati.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{gujarati}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/hindi.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{hindi}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/kannada.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{kannada}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/malayalam.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{malayalam}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/marathi.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{marathi}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/oriya.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{oriya}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/odia.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{odia}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/panjabi.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{panjabi}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/tamil.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{tamil}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/telugu.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{telugu}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-sanskrit
Provides:       tex-hyphen-sanskrit = %{tl_version}
License:        LPPL
Summary:        Sanskrit hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-sanskrit
Hyphenation patterns for Sanskrit and Prakrit in
transliteration, and in Devanagari, Bengali, Kannada, Malayalam
and Telugu scripts for Unicode engines.

%post -n texlive-hyphen-sanskrit
if [ $1 -gt 0 ] ; then
sed -i '/sanskrit.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "sanskrit loadhyph-sa.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{sanskrit}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{sanskrit}{loadhyph-sa.tex}{}{1}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-sanskrit
if [ $1 == 0 ] ; then
sed -i '/sanskrit.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{sanskrit}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-italian
Provides:       tex-hyphen-italian = %{tl_version}
License:        LGPLv2+
Summary:        Italian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-italian
Hyphenation patterns for Italian in ASCII encoding. Compliant
with the Recommendation UNI 6461 on hyphenation issued by the
Italian Standards Institution (Ente Nazionale di Unificazione
UNI).

%post -n texlive-hyphen-italian
if [ $1 -gt 0 ] ; then
sed -i '/italian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "italian loadhyph-it.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{italian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{italian}{loadhyph-it.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-italian
if [ $1 == 0 ] ; then
sed -i '/italian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{italian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-ipaex
Provides:       tex-ipaex = %{tl_version}
License:        IPA
Summary:        IPA and IPAex fonts from Information-technology Promotion Agency, Japan
Version:        svn45751
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(ipaexg.ttf) = %{tl_version}, tex(ipaexm.ttf) = %{tl_version}
Provides:       tex(ipag.ttf) = %{tl_version}, tex(ipagp.ttf) = %{tl_version}
Provides:       tex(ipam.ttf) = %{tl_version}, tex(ipamp.ttf) = %{tl_version}

%description -n texlive-ipaex
The fonts provide fixed-width glyphs for Kana and Kanji
characters, proportional width glyphs for Western characters.

%package -n texlive-ipaex-doc
Summary:        Documentation for ipaex
Version:        svn45751
Provides:       tex-ipaex-doc
AutoReqProv:    No

%description -n texlive-ipaex-doc
Documentation for ipaex

%package -n texlive-hyphen-afrikaans
Provides:       tex-hyphen-afrikaans = %{tl_version}
License:        LPPL
Summary:        Afrikaans hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-afrikaans
Hyphenation patterns for Afrikaans in T1/EC and UTF-8
encodings. OpenOffice includes older patterns created by a
different author, but the patterns packaged with TeX are
considered superior in quality.

%post -n texlive-hyphen-afrikaans
if [ $1 -gt 0 ] ; then
sed -i '/afrikaans.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "afrikaans loadhyph-af.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{afrikaans}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{afrikaans}{loadhyph-af.tex}{}{1}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-afrikaans
if [ $1 == 0 ] ; then
sed -i '/afrikaans.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{afrikaans}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-coptic
Provides:       tex-hyphen-coptic = %{tl_version}
License:        LPPL
Summary:        Coptic hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-coptic
Hyphenation patterns for Coptic in UTF-8 encoding as well as in
ASCII-based encoding for 8-bit engines. The latter can only be
used with special Coptic fonts (like CBcoptic). The patterns
are considered experimental.

%post -n texlive-hyphen-coptic
if [ $1 -gt 0 ] ; then
sed -i '/coptic.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "coptic loadhyph-cop.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{coptic}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{coptic}{loadhyph-cop.tex}{}{1}{1}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-coptic
if [ $1 == 0 ] ; then
sed -i '/coptic.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{coptic}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-esperanto
Provides:       tex-hyphen-esperanto = %{tl_version}
License:        LPPL
Summary:        Esperanto hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-esperanto
Hyphenation patterns for Esperanto ISO Latin 3 and UTF-8
encodings. Note that TeX distributions don't ship any suitable
fonts in Latin 3 encoding, so unless you create your own font
support or want to use MlTeX, using native Unicode engines is
highly recommended.

%post -n texlive-hyphen-esperanto
if [ $1 -gt 0 ] ; then
sed -i '/esperanto.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "esperanto loadhyph-eo.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{esperanto}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{esperanto}{loadhyph-eo.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-esperanto
if [ $1 == 0 ] ; then
sed -i '/esperanto.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{esperanto}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-georgian
Provides:       tex-hyphen-georgian = %{tl_version}
License:        LPPL
Summary:        Georgian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-georgian
Hyphenation patterns for Georgian in T8M, T8K and UTF-8
encodings.

%post -n texlive-hyphen-georgian
if [ $1 -gt 0 ] ; then
sed -i '/georgian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "georgian loadhyph-ka.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{georgian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{georgian}{loadhyph-ka.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-georgian
if [ $1 == 0 ] ; then
sed -i '/georgian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{georgian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-indonesian
Provides:       tex-hyphen-indonesian = %{tl_version}
License:        LPPL
Summary:        Indonesian hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-indonesian
Hyphenation patterns for Indonesian (Bahasa Indonesia) in ASCII
encoding.  They are probably also usable for Malay (Bahasa
Melayu).

%post -n texlive-hyphen-indonesian
if [ $1 -gt 0 ] ; then
sed -i '/indonesian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "indonesian loadhyph-id.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{indonesian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{indonesian}{loadhyph-id.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-indonesian
if [ $1 == 0 ] ; then
sed -i '/indonesian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{indonesian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-interlingua
Provides:       tex-hyphen-interlingua = %{tl_version}
License:        LPPL
Summary:        Interlingua hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-interlingua
Hyphenation patterns for Interlingua in ASCII encoding.

%post -n texlive-hyphen-interlingua
if [ $1 -gt 0 ] ; then
sed -i '/interlingua.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "interlingua loadhyph-ia.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{interlingua}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{interlingua}{loadhyph-ia.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-interlingua
if [ $1 == 0 ] ; then
sed -i '/interlingua.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{interlingua}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-thai
Provides:       tex-hyphen-thai = %{tl_version}
License:        LPPL
Summary:        Thai hyphenation patterns
Version:        svn47375
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils
Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-thai
Hyphenation patterns for Thai in LTH and UTF-8 encodings.

%post -n texlive-hyphen-thai
if [ $1 -gt 0 ] ; then
sed -i '/thai.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "thai loadhyph-th.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{thai}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{thai}{loadhyph-th.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-thai
if [ $1 == 0 ] ; then
sed -i '/thai.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{thai}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-turkmen
Provides:       tex-hyphen-turkmen = %{tl_version}
License:        LPPL
Summary:        Turkmen hyphenation patterns
Version:        svn41113

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-turkmen
Hyphenation patterns for Turkmen in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-turkmen
if [ $1 -gt 0 ] ; then
sed -i '/turkmen.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "turkmen loadhyph-tk.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{turkmen}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{turkmen}{loadhyph-tk.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-turkmen
if [ $1 == 0 ] ; then
sed -i '/turkmen.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{turkmen}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-polish
Provides:       tex-hyphen-polish = %{tl_version}
License:        Knuth
Summary:        Polish hyphenation patterns
Version:        svn41113

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-polish
Hyphenation patterns for Polish in QX and UTF-8 encodings.
These patterns are also used by Polish TeX formats MeX and
LaMeX.

%post -n texlive-hyphen-polish
if [ $1 -gt 0 ] ; then
sed -i '/polish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "polish loadhyph-pl.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{polish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{polish}{loadhyph-pl.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-polish
if [ $1 == 0 ] ; then
sed -i '/polish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{polish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-portuguese
Provides:       tex-hyphen-portuguese = %{tl_version}
License:        LPPL
Summary:        Portuguese hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-portuguese
Hyphenation patterns for Portuguese in T1/EC and UTF-8
encodings.

%post -n texlive-hyphen-portuguese
if [ $1 -gt 0 ] ; then
sed -i '/portuguese.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "portuguese loadhyph-pt.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=portuges/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=portuges" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=brazil/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=brazil" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=brazilian/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=brazilian" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{portuguese}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{portuguese}{loadhyph-pt.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{portuges}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{portuges}{loadhyph-pt.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{brazil}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{brazil}{loadhyph-pt.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{brazilian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{brazilian}{loadhyph-pt.tex}{}{2}{3}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-portuguese
if [ $1 == 0 ] ; then
sed -i '/portuguese.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=portuges/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=brazil/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=brazilian/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{portuguese}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{portuges}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{brazil}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{brazilian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-catalan
Provides:       tex-hyphen-catalan = %{tl_version}
License:        LPPL
Summary:        Catalan hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-catalan
Hyphenation patterns for Catalan in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-catalan
if [ $1 -gt 0 ] ; then
sed -i '/catalan.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "catalan loadhyph-ca.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{catalan}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{catalan}{loadhyph-ca.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-catalan
if [ $1 == 0 ] ; then
sed -i '/catalan.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{catalan}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-galician
Provides:       tex-hyphen-galician = %{tl_version}
License:        LPPL
Summary:        Galician hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-galician
Hyphenation patterns for Galician in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-galician
if [ $1 -gt 0 ] ; then
sed -i '/galician.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "galician loadhyph-gl.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{galician}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{galician}{loadhyph-gl.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-galician
if [ $1 == 0 ] ; then
sed -i '/galician.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{galician}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-hyphen-spanish
Provides:       tex-hyphen-spanish = %{tl_version}
License:        LPPL
Summary:        Spanish hyphenation patterns
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Requires(post,postun): coreutils

Requires:       tex-hyphen-base, tex-hyph-utf8

%description -n texlive-hyphen-spanish
Hyphenation patterns for Spanish in T1/EC and UTF-8 encodings.

%post -n texlive-hyphen-spanish
if [ $1 -gt 0 ] ; then
sed -i '/spanish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "spanish loadhyph-es.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/=espanol/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "=espanol" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{spanish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{spanish}{loadhyph-es.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
sed -i '/\\addlanguage{espanol}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{espanol}{loadhyph-es.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-spanish
if [ $1 == 0 ] ; then
sed -i '/spanish.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
  sed -i '/=espanol/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{spanish}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
sed -i '/\\addlanguage{espanol}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-index
Provides:       tex-index = %{tl_version}
License:        LPPL
Summary:        Extended index for LaTeX including multiple indexes
Version:        svn24099.4.1beta

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(autind.sty) = %{tl_version}, tex(bibref.sty) = %{tl_version}
Provides:       tex(index.sty) = %{tl_version}

%description -n texlive-index
This is a reimplementation of LaTeX's indexing macros to
provide better support for indexing. For example, it supports
multiple indexes in a single document and provides a more
robust \index command. It supplies short hand notations for the
\index command (^{word}) and a * variation of \index
(abbreviated _{word}) that prints the word being indexed, as
well as creating an index entry for it.

%package -n texlive-index-doc
Summary:        Documentation for index
Version:        svn24099.4.1beta

Provides:       tex-index-doc
AutoReqProv:    No

%description -n texlive-index-doc
Documentation for index

%package -n texlive-ifmtarg
Provides:       tex-ifmtarg = %{tl_version}
License:        LPPL
Summary:        If-then-else command for processing potentially empty arguments
Version:        svn47544
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(ifmtarg.sty) = %{tl_version}

%description -n texlive-ifmtarg
ifmtarg package

%package -n texlive-ifmtarg-doc
Summary:        Documentation for ifmtarg
Version:        svn47544
Provides:       tex-ifmtarg-doc
AutoReqProv:    No

%description -n texlive-ifmtarg-doc
Documentation for ifmtarg

%package -n texlive-hypdvips
Provides:       tex-hypdvips = %{tl_version}
License:        LPPL 1.3
Summary:        Hyperref extensions for use with dvips
Version:        svn34364.3.02

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(atveryend.sty), tex(xcolor.sty), tex(xkeyval.sty), tex(bookmark.sty)
Requires:       tex(hypcap.sty)
Provides:       tex(hypdvips.sty) = %{tl_version}

%description -n texlive-hypdvips
The hypdvips package fixes some problems when using hyperref
with dvips. It also adds support for breaking links, file
attachments, embedded documents and different types of GoTo-
links. The cooperation of hyperref with cleveref is improved,
which in addition allows an enhanced back-referencing system.

%package -n texlive-hypdvips-doc
Summary:        Documentation for hypdvips
Version:        svn34364.3.02

Provides:       tex-hypdvips-doc
AutoReqProv:    No

%description -n texlive-hypdvips-doc
Documentation for hypdvips

%package -n texlive-hyper
Provides:       tex-hyper = %{tl_version}
License:        LPPL
Summary:        Hypertext cross referencing
Version:        svn17357.4.2d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(defpattern.sty), tex(color.sty)
Provides:       tex(hxt-bc.sty) = %{tl_version}, tex(hyper.sty) = %{tl_version}

%description -n texlive-hyper
Redefines LaTeX cross-referencing commands to insert \special
commands for HyperTeX dvi viewers, such as recent versions of
xdvi. The package is now largely superseded by hyperref.

%package -n texlive-hyper-doc
Summary:        Documentation for hyper
Version:        svn17357.4.2d

Provides:       tex-hyper-doc
AutoReqProv:    No

%description -n texlive-hyper-doc
Documentation for hyper

%package -n texlive-hypernat
Provides:       tex-hypernat = %{tl_version}
License:        GPL+
Summary:        Allow hyperref and natbib to work together
Version:        svn17358.1.0b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(hypernat.sty) = %{tl_version}

%description -n texlive-hypernat
Allows hyperref package and the natbib package with options
'numbers' and 'sort&compress' to work together. This means that
multiple sequential citations (e.g [3,2,1]) will be compressed
to [1-3], where the '1' and the '3' are (color-)linked to the
bibliography.

%package -n texlive-hypernat-doc
Summary:        Documentation for hypernat
Version:        svn17358.1.0b

Provides:       tex-hypernat-doc
AutoReqProv:    No

%description -n texlive-hypernat-doc
Documentation for hypernat

%package -n texlive-hyperxmp
Provides:       tex-hyperxmp = %{tl_version}
License:        LPPL 1.3
Summary:        Embed XMP metadata within a LaTeX document
Version:        svn46073
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(atenddvi.sty), tex(kvoptions.sty), tex(pdfescape.sty), tex(stringenc.sty)
Requires:       tex(intcalc.sty), tex(ifxetex.sty)
Provides:       tex(hyperxmp.sty) = %{tl_version}

%description -n texlive-hyperxmp
XMP (eXtensible Metadata Platform) is a mechanism proposed by
Adobe for embedding document metadata within the document
itself. The metadata is designed to be easy to extract, even by
programs that are oblivious to the document's file format. Most
of Adobe's applications store XMP metadata when saving files.
Now, with the hyperxmp package, it is trivial for LaTeX
document authors to store XMP metadata in their documents as
well. Version 2.2 of the package added support for the IPTC
Photo Metadata schema. It allows \xmpcomma and \xmpquote to be
used in any hyperxmp option, not only those that require
special treatment of commas. And it introduces an \xmplinesep
macro that controls how multiline fields are represented in the
XMP packet. The package integrates seamlessly with hyperref and
requires virtually no modifications to documents that already
exploit hyperref's mechanisms for specifying PDF metadata. The
current version of hyperxmp can embed the following metadata as
XMP: title, authors, primary author's title or position,
metadata writer, subject/summary, keywords, copyright, license
URL, document base URL, document identifier and instance
identifier, language, source file name, PDF generating tool,
PDF version, and contact telephone number/postal address/email
address/URL. Hyperxmp currently embeds XMP only within PDF
documents; it is compatible with pdflatex, xelatex,
latex+dvipdfm, and latex+dvips+ps2pdf.

%package -n texlive-hyperxmp-doc
Summary:        Documentation for hyperxmp
Version:        svn46073
Provides:       tex-hyperxmp-doc
AutoReqProv:    No

%description -n texlive-hyperxmp-doc
Documentation for hyperxmp

%package -n texlive-hyphenat
Provides:       tex-hyphenat = %{tl_version}
License:        LPPL 1.3
Summary:        Disable/enable hypenation
Version:        svn15878.2.3c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(hyphenat.sty) = %{tl_version}

%description -n texlive-hyphenat
This package can disable all hyphenation or enable hyphenation
of non-alphabetics or monospaced fonts. The package can also
enable hyphenation within 'words' that contain non-alphabetic
characters (e.g., that include underscores), and hyphenation of
text typeset in monospaced (e.g., cmtt) fonts.

%package -n texlive-hyphenat-doc
Summary:        Documentation for hyphenat
Version:        svn15878.2.3c

Provides:       tex-hyphenat-doc
AutoReqProv:    No

%description -n texlive-hyphenat-doc
Documentation for hyphenat

%package -n texlive-idxcmds
Provides:       tex-idxcmds = %{tl_version}
License:        LPPL 1.3
Summary:        Semantic commands for adding formatted index entries
Version:        svn38115.0.2c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(pgfopts.sty), tex(ltxcmds.sty)
Provides:       tex(idxcmds.sty) = %{tl_version}

%description -n texlive-idxcmds
The package provides commands for adding formatted index
entries; it arises from the author's work on large documents.

%package -n texlive-idxcmds-doc
Summary:        Documentation for idxcmds
Version:        svn38115.0.2c

Provides:       tex-idxcmds-doc
AutoReqProv:    No

%description -n texlive-idxcmds-doc
Documentation for idxcmds

%package -n texlive-idxlayout
Provides:       tex-idxlayout = %{tl_version}
License:        LPPL
Summary:        Configurable index layout, responsive to KOMA-Script and memoir
Version:        svn25821.0.4d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(kvoptions.sty), tex(multicol.sty), tex(ragged2e.sty)
Provides:       tex(idxlayout.sty) = %{tl_version}

%description -n texlive-idxlayout
The idxlayout package offers a key-value interface to configure
index layout parameters, e.g. allowing for three-column indexes
or for "parent" items and their affiliated subitems being
typeset as a single paragraph. The package is responsive to the
index-related options and commands of the KOMA-Script and
memoir classes.

%package -n texlive-idxlayout-doc
Summary:        Documentation for idxlayout
Version:        svn25821.0.4d

Provides:       tex-idxlayout-doc
AutoReqProv:    No

%description -n texlive-idxlayout-doc
Documentation for idxlayout

%package -n texlive-ifmslide
Provides:       tex-ifmslide = %{tl_version}
License:        LPPL 1.2
Summary:        Presentation slides for screen and printouts
Version:        svn20727.0.47

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(hyperref.sty), tex(ifpdf.sty), tex(color.sty), tex(texpower.sty)
Requires:       tex(fixseminar.sty), tex(ifthen.sty), tex(calc.sty), tex(graphicx.sty)
Requires:       tex(amssymb.sty), tex(amsbsy.sty)
Provides:       tex(ifmslide.cfg) = %{tl_version}, tex(ifmslide.sty) = %{tl_version}

%description -n texlive-ifmslide
This package is used to produce printed slides with LaTeX and
online presentations with pdfLaTeX. It is provided by the
'Institute of Mechanics' (ifm) Univ. of Technology Darmstadt,
Germany. It is based on ideas of pdfslide, but completely
rewritten for compatibility with texpower and seminar. The
manual describes all functions and provides a sample.

%package -n texlive-ifmslide-doc
Summary:        Documentation for ifmslide
Version:        svn20727.0.47

Provides:       tex-ifmslide-doc
AutoReqProv:    No

%description -n texlive-ifmslide-doc
Documentation for ifmslide

%package -n texlive-ifnextok
Provides:       tex-ifnextok = %{tl_version}
License:        LPPL 1.3
Summary:        Utility macro: peek ahead without ignoring spaces
Version:        svn23379.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ifnextok.sty) = %{tl_version}

%description -n texlive-ifnextok
The package deals with the behaviour of the LaTeX internal
command \@ifnextchar, which skips blank spaces. This has the
potential to surprise users, since it can produce really
unwanted effects. A common example occurs with brackets
starting a line following \\: the command looks for an optional
argument, whereas the user wants the brackets to be printed.
The package offers commands and options for modifying this
behaviour, maybe limited to certain parts of the document
source.

%package -n texlive-ifnextok-doc
Summary:        Documentation for ifnextok
Version:        svn23379.0.3

Provides:       tex-ifnextok-doc
AutoReqProv:    No

%description -n texlive-ifnextok-doc
Documentation for ifnextok

%package -n texlive-ifoddpage
Provides:       tex-ifoddpage = %{tl_version}
License:        LPPL 1.3
Summary:        Determine if the current page is odd or even
Version:        svn40726

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ifoddpage.sty) = %{tl_version}

%description -n texlive-ifoddpage
The package provides an \ifoddpage conditional to determine if
the current page is odd or even. The macro \checkoddpage must
be used direct before to check the page number using a label.
Two compiler runs are therefore required to achieve correct
results. In addition, the conditional \ifoddpageoronside is
provided which is also true in oneside mode where all pages use
the odd page layout.

%package -n texlive-ifoddpage-doc
Summary:        Documentation for ifoddpage
Version:        svn40726

Provides:       tex-ifoddpage-doc
AutoReqProv:    No

%description -n texlive-ifoddpage-doc
Documentation for ifoddpage

%package -n texlive-ifplatform
Provides:       tex-ifplatform = %{tl_version}
License:        LPPL
Summary:        Conditionals to test which platform is being used
Version:        svn45533
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pdftexcmds.sty), tex(catchfile.sty), tex(ifluatex.sty)
Provides:       tex(ifplatform.sty) = %{tl_version}

%description -n texlive-ifplatform
This package uses the (La)TeX extension -shell-escape to
establish whether the document is being processed on a Windows
or on a Unix-like system (Mac OS X, Linux, etc.), or on Cygwin
(Unix environment over a windows system). Booleans provided
are: \ifwindows, \iflinux, \ifmacosx and \ifcygwin. The package
also preserves the output of uname on a Unix-like system, which
may be used to distinguish between various classes of Unix
systems.

%package -n texlive-ifplatform-doc
Summary:        Documentation for ifplatform
Version:        svn45533
Provides:       tex-ifplatform-doc
AutoReqProv:    No

%description -n texlive-ifplatform-doc
Documentation for ifplatform

%package -n texlive-ifthenx
Provides:       tex-ifthenx = %{tl_version}
License:        LPPL
Summary:        Extra tests for \ifthenelse
Version:        svn25819.0.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(ifthenx.sty) = %{tl_version}

%description -n texlive-ifthenx
The package extends the ifthen package, providing extra
predicates for the package's \ifthenelse command. The package
is complementary to xifthen, in that they provide different
facilities; the two may be loaded in the same document, as long
as xifthen is loaded first.

%package -n texlive-ifthenx-doc
Summary:        Documentation for ifthenx
Version:        svn25819.0.1a

Provides:       tex-ifthenx-doc
AutoReqProv:    No

%description -n texlive-ifthenx-doc
Documentation for ifthenx

%package -n texlive-iitem
Provides:       tex-iitem = %{tl_version}
License:        LPPL
Summary:        Multiple level of lists in one list-like environment
Version:        svn29613.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(iitem.sty) = %{tl_version}

%description -n texlive-iitem
The package defines multiple level lists within one list-like
environment. instead of writing \begin{enumerate} \item 1
\begin{enumerate} \item 2 \begin{enumerate} \item 3
\begin{enumerate} \item 4 \end{enumerate} \end{enumerate} \item
2.1 \end{enumerate} \item 1.1 \begin{enumerate} \item 2
\end{enumerate} \end{enumerate} this package allows you to
write \begin{enumerate} \item 1 \iitem 2 \iiitem 3 \ivtem 4
\iitem 2.1 \item 1.1 \iitem 2 \end{enumerate}

%package -n texlive-iitem-doc
Summary:        Documentation for iitem
Version:        svn29613.1.0

Provides:       tex-iitem-doc
AutoReqProv:    No

%description -n texlive-iitem-doc
Documentation for iitem

%package -n texlive-image-gallery
Provides:       tex-image-gallery = %{tl_version}
License:        LPPL
Summary:        Create an overview of pictures from a digital camera or from other sources
Version:        svn15878.v1.0j

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(graphicx.sty), tex(keyval.sty), tex(url.sty)
Requires:       tex(geometry.sty)
Provides:       tex(image-gallery.cls) = %{tl_version}

%description -n texlive-image-gallery
The class may be used to create an overview of pictures from a
digital camera or from other sources. It is possible to adjust
the size of the pictures and all the margins. The example file
shows the usage.

%package -n texlive-image-gallery-doc
Summary:        Documentation for image-gallery
Version:        svn15878.v1.0j

Provides:       tex-image-gallery-doc
AutoReqProv:    No

%description -n texlive-image-gallery-doc
Documentation for image-gallery

%package -n texlive-imakeidx
Provides:       tex-imakeidx = %{tl_version}
License:        LPPL 1.3
Summary:        A package for producing multiple indexes
Version:        svn42287
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(ifxetex.sty), tex(ifluatex.sty), tex(pdftexcmds.sty)
Requires:       tex(xpatch.sty), tex(multicol.sty)
Provides:       tex(imakeidx.sty) = %{tl_version}

%description -n texlive-imakeidx
The package enables the user to produce and typeset one or more
indexes simultaneously with a document. The package is known to
work in LaTeX documents processed with pdflatex, xelatatex and
lualatex. If makeindex is used for processing the index
entries, no particular setting up is needed when TeX Live is
used. Using xindy or other programs it is necessary to enable
shell escape; shell escape is also needed if splitindex is
used.

%package -n texlive-imakeidx-doc
Summary:        Documentation for imakeidx
Version:        svn42287
Provides:       tex-imakeidx-doc
AutoReqProv:    No

%description -n texlive-imakeidx-doc
Documentation for imakeidx

%package -n texlive-import
Provides:       tex-import = %{tl_version}
License:        Public Domain
Summary:        Establish input relative to a directory
Version:        svn17361.5.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(import.sty) = %{tl_version}

%description -n texlive-import
The commands \import{full_path}{file} and
\subimport{path_extension}{file} set up input through standard
LaTeX mechanisms (\input, \include and \includegraphics) to
load files relative to the \import-ed directory. There are also
\includefrom, \subincludefrom, and * variants of the commands.

%package -n texlive-import-doc
Summary:        Documentation for import
Version:        svn17361.5.1

Provides:       tex-import-doc
AutoReqProv:    No

%description -n texlive-import-doc
Documentation for import

%package -n texlive-incgraph
Provides:       tex-incgraph = %{tl_version}
License:        LPPL 1.3
Summary:        Sophisticated graphics inclusion in a PDF document
Version:        svn36500.1.12

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pgf.sty), tex(pgffor.sty), tex(graphicx.sty), tex(bookmark.sty)
Requires:       tex(pgfkeys.sty)
Provides:       tex(incgraph.sty) = %{tl_version}

%description -n texlive-incgraph
The package provides tools for including graphics at the full
size of the output medium, or for creating "pages" whose size
is that of the graphic they contain. A principal use case is
documents that require inclusion of (potentially many) scans or
photographs. Bookmarking is especially supported. The tool box
has basic macros and a 'convenience' user interface that wraps
\includegraphics.

%package -n texlive-incgraph-doc
Summary:        Documentation for incgraph
Version:        svn36500.1.12

Provides:       tex-incgraph-doc
AutoReqProv:    No

%description -n texlive-incgraph-doc
Documentation for incgraph

%package -n texlive-indextools
Provides:       tex-indextools = %{tl_version}
License:        LPPL 1.3
Summary:        A fork of imakeidx to fixe one bug with bidi
Version:        svn38931

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(ifxetex.sty), tex(ifluatex.sty), tex(pdftexcmds.sty)
Requires:       tex(xpatch.sty), tex(multicol.sty)
Provides:       tex(indextools.sty) = %{tl_version}

%description -n texlive-indextools
This package is a fork of the imakeidx package. The original
authors of imakeidx declined some upgrade suggestions to remove
incompatibilities with certain packages that are particularly
important with critical editions dealing with languages that
are being written from right to left. Therefore this fork was
created in order to let other users benefit from its
functionalities very useful in the field of humanities.

%package -n texlive-indextools-doc
Summary:        Documentation for indextools
Version:        svn38931

Provides:       tex-indextools-doc
AutoReqProv:    No

%description -n texlive-indextools-doc
Documentation for indextools

%package -n texlive-inlinedef
Provides:       tex-inlinedef = %{tl_version}
License:        LPPL
Summary:        Inline expansions within definitions
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(inlinedef.sty) = %{tl_version}

%description -n texlive-inlinedef
The package provides a macro \Inline that precedes a \def or
\gdef. Within the definition text of an inlined definition,
keywords such as \Expand may be used to selectively inline
certain expansions at definition-time. This eases the process
of redefining macros in terms of the original definition, as
well as definitions in which the token that must be expanded is
deep within, where \expandafter would be difficult and \edef is
not suitable. Another application is as an easier version of
\aftergroup, by defining a macro in terms of expanded local
variables, then ending the group with
\expandafter\endgroup\macro.

%package -n texlive-inlinedef-doc
Summary:        Documentation for inlinedef
Version:        svn15878.1.0

Provides:       tex-inlinedef-doc
AutoReqProv:    No

%description -n texlive-inlinedef-doc
Documentation for inlinedef

%package -n texlive-inputtrc
Provides:       tex-inputtrc = %{tl_version}
License:        LPPL 1.3
Summary:        Trace which file loads which
Version:        svn28019.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(inputtrc.sty) = %{tl_version}

%description -n texlive-inputtrc
The package produces screen/log messages of the form '<current>
INPUTTING <next>' reporting LaTeX input commands (<current> and
<next> being file names). The message is indented to reflect
the level of input nesting. Tracing may be turned on and off,
and the unit of indentation may be adjusted. The implementation
somewhat resembles those of packages FiNK and inputfile.

%package -n texlive-inputtrc-doc
Summary:        Documentation for inputtrc
Version:        svn28019.0.3

Provides:       tex-inputtrc-doc
AutoReqProv:    No

%description -n texlive-inputtrc-doc
Documentation for inputtrc

%package -n texlive-interactiveworkbook
Provides:       tex-interactiveworkbook = %{tl_version}
License:        LPPL
Summary:        LaTeX-based interactive PDF on the Web
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(epsfig.sty), tex(color.sty), tex(xspace.sty), tex(ifthen.sty)
Provides:       tex(interactiveworkbook-web.sty) = %{tl_version}
Provides:       tex(interactiveworkbook.sty) = %{tl_version}
Provides:       tex(interactiveworkbook.sty) = %{tl_version}

%description -n texlive-interactiveworkbook
The package interactiveworkbook gives the user the ability to
write LaTeX documents which, ultimately, create interactive
question-and-answer Portable Document Format (PDF) tutorials
meant to be used by Internet students and that, in particular,
freely use mathematical notation.

%package -n texlive-interactiveworkbook-doc
Summary:        Documentation for interactiveworkbook
Version:        svn15878.0

Provides:       tex-interactiveworkbook-doc
AutoReqProv:    No

%description -n texlive-interactiveworkbook-doc
Documentation for interactiveworkbook

%package -n texlive-interfaces
Provides:       tex-interfaces = %{tl_version}
License:        LPPL 1.3
Summary:        Set parameters for other packages, conveniently
Version:        svn21474.3.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(ltxcmds.sty), tex(etoolbox.sty), tex(pgfkeys.sty)
Requires:       tex(scrlfile.sty), tex(infwarerr.sty), tex(interfaces-scrlfile.sty), tex(interfaces-tikz.sty)
Requires:       tex(interfaces-marks.sty), tex(refcount.sty)
Requires:       tex(gettitlestring.sty), tex(tikz.sty), tex(auxhook.sty)
Provides:       tex(interfaces-LaTeX.sty) = %{tl_version}
Provides:       tex(interfaces-appendix.sty) = %{tl_version}
Provides:       tex(interfaces-base.sty) = %{tl_version}
Provides:       tex(interfaces-bookmark.sty) = %{tl_version}
Provides:       tex(interfaces-embedfile.sty) = %{tl_version}
Provides:       tex(interfaces-enumitem.sty) = %{tl_version}
Provides:       tex(interfaces-environ.sty) = %{tl_version}
Provides:       tex(interfaces-etoolbox.sty) = %{tl_version}
Provides:       tex(interfaces-fancyhdr.sty) = %{tl_version}
Provides:       tex(interfaces-hypbmsec.sty) = %{tl_version}
Provides:       tex(interfaces-hyperref.sty) = %{tl_version}
Provides:       tex(interfaces-makecell.sty) = %{tl_version}
Provides:       tex(interfaces-marks.sty) = %{tl_version}
Provides:       tex(interfaces-pgfkeys.sty) = %{tl_version}
Provides:       tex(interfaces-scrlfile.sty) = %{tl_version}
Provides:       tex(interfaces-tikz.sty) = %{tl_version}
Provides:       tex(interfaces-titlesec.sty) = %{tl_version}
Provides:       tex(interfaces-tocloft.sty) = %{tl_version}
Provides:       tex(interfaces-truncate.sty) = %{tl_version}
Provides:       tex(interfaces-umrand.sty) = %{tl_version}
Provides:       tex(interfaces.sty) = %{tl_version}

%description -n texlive-interfaces
The package provides a small number of convenient macros that
access features in other frequently-used packages, or provide
interfaces to other useful facilities such as the pdfTeX
\pdfelapsedtime primitive. Most of these macros use pgfkeys to
provide a key-value syntax. The package also uses the package
scrlfile from the Koma-Script bundle (for controlled loading of
other files) and etoolbox. The package is bundled with sub-
packages containing actual interfaces: by default, the package
loads all available sub-packages, but techniques are provided
for the user to select no more than the interfaces needed for a
job.

%package -n texlive-interfaces-doc
Summary:        Documentation for interfaces
Version:        svn21474.3.1

Provides:       tex-interfaces-doc
AutoReqProv:    No

%description -n texlive-interfaces-doc
Documentation for interfaces

%package -n texlive-inversepath
Provides:       tex-inversepath = %{tl_version}
License:        LPPL 1.3
Summary:        Calculate inverse file paths
Version:        svn15878.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(inversepath.sty) = %{tl_version}

%description -n texlive-inversepath
The package calculates inverse relative paths. Such things may
be useful, for example, when writing an auxiliary file to a
different directory.

%package -n texlive-inversepath-doc
Summary:        Documentation for inversepath
Version:        svn15878.0.2

Provides:       tex-inversepath-doc
AutoReqProv:    No

%description -n texlive-inversepath-doc
Documentation for inversepath

%package -n texlive-invoice
Provides:       tex-invoice = %{tl_version}
License:        GPL+
Summary:        Generate invoices
Version:        svn48359
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(longtable.sty), tex(calc.sty), tex(fp.tex)
Provides:       tex(invoice.def) = %{tl_version}, tex(invoice.sty) = %{tl_version}

%description -n texlive-invoice
The package may be used for generating invoices. The package
can deal with invisible expense items and deductions; output
may be presented in any of 10 different languages. The package
depends on the fp and calc packages for its calculations.

%package -n texlive-invoice-doc
Summary:        Documentation for invoice
Version:        svn48359
Provides:       tex-invoice-doc
AutoReqProv:    No

%description -n texlive-invoice-doc
Documentation for invoice

%package -n texlive-interpreter
Provides:       tex-interpreter = %{tl_version}
License:        LPPL
Summary:        Translate input files on the fly
Version:        svn27232.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(interpreter.sty) = %{tl_version}, tex(interpreter.tex) = %{tl_version}

%description -n texlive-interpreter
The package preprocesses input files to a Lua(La)TeX run, on
the fly. The user defines Lua regular expressions to search for
patterns and modify input lines (or entire paragraphs)
accordingly, before TeX reads the material. In this way,
documents may be prepared in a non-TeX language (e.g., some
lightweight markup language) and turned into 'proper' TeX for
processing. The source of the documentation is typed in such a
lightweight language and is thus easily readable in a text
editor (the PDF file is also available, of course); the
transformation to TeX syntax via Interpreter's functions is
explained in the documentation itself. Interpreter is
implemented using the author's gates (lua version), and works
for plain TeX and LaTeX, but not ConTeXt.

%package -n texlive-interpreter-doc
Summary:        Documentation for interpreter
Version:        svn27232.1.2

Provides:       tex-interpreter-doc
AutoReqProv:    No

%description -n texlive-interpreter-doc
Documentation for interpreter

%package -n texlive-interval
Provides:       tex-interval = %{tl_version}
License:        LPPL 1.3
Summary:        Format mathematical intervals, ensuring proper spacing
Version:        svn34840.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pgfkeys.sty)
Provides:       tex(interval.sty) = %{tl_version}

%description -n texlive-interval
When typing an open interval as $]a,b[$, a closing bracket is
being used in place of an opening fence and vice versa. This
leads to the wrong spacing in, say, $]-a,b[$ or $A\in]a,b[=B$.
The package attempts to solve this using: \interval{a}{b} ->
[a,b] \interval[open]{a}{b} -> ]a,b[ \interval[open left]{a}{b}
-> ]a,b] The package also supports fence scaling and ensures
that the enclosing fences will end up having the proper closing
and opening types. TeX maths does not do this job properly.

%package -n texlive-interval-doc
Summary:        Documentation for interval
Version:        svn34840.0.3

Provides:       tex-interval-doc
AutoReqProv:    No

%description -n texlive-interval-doc
Documentation for interval

%package -n texlive-ionumbers
Provides:       tex-ionumbers = %{tl_version}
License:        GPL+
Summary:        Restyle numbers in maths mode
Version:        svn33457.0.3.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(ionumbers.sty) = %{tl_version}

%description -n texlive-ionumbers
'ionumbers' stands for 'input/output numbers'. The package
restyles numbers in maths mode. If a number in the input file
is written, e.g., as $3,231.44$ as commonly used in English
texts, the package is able to restyle it to be output as
$3\,231{,}44$ as commonly used in German texts (and vice
versa). This may be useful, for example, if you have a large
table and want to include it in texts with different output
conventions without the need to change the table. The package
can also automatically group digits left of the decimal
separator (thousands) and right of the decimal separator
(thousandths) in triplets without the need of specifing commas
(English) or points (German) as separators. E.g., the input
$1234.567890$ can be output as $1\,234.\,567\,890$. Finally, an
e starts the exponent of the number. For example, $21e6$ may be
output as $26\times10\,^{6}$.

%package -n texlive-ionumbers-doc
Summary:        Documentation for ionumbers
Version:        svn33457.0.3.3

Provides:       tex-ionumbers-doc
AutoReqProv:    No

%description -n texlive-ionumbers-doc
Documentation for ionumbers

%package -n texlive-hyplain
Provides:       tex-hyplain = %{tl_version}
License:        Public Domain
Summary:        Basic support for multiple languages in Plain TeX
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(hylang.tex) = %{tl_version}, tex(hyplain.tex) = %{tl_version}
Provides:       tex(hyrules.tex) = %{tl_version}

%description -n texlive-hyplain
The package offers a means to set up hyphenation suitable for
several languages and/or dialects, and to select them or switch
between them while typesetting.

%package -n texlive-hyplain-doc
Summary:        Documentation for hyplain
Version:        svn15878.1.0

Provides:       tex-hyplain-doc
AutoReqProv:    No

%description -n texlive-hyplain-doc
Documentation for hyplain

%package -n texlive-icsv
Provides:       tex-icsv = %{tl_version}
License:        LPPL
Summary:        Class for typesetting articles for the ICSV conference
Version:        svn15878.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(amsmath.sty), tex(amssymb.sty), tex(array.sty)
Requires:       tex(bm.sty), tex(calc.sty), tex(fancyhdr.sty), tex(fixltx2e.sty)
Requires:       tex(fix-cm.sty), tex(graphicx.sty), tex(hyperref.sty), tex(ifthen.sty)
Requires:       tex(caption.sty), tex(helvet.sty), tex(fontenc.sty), tex(textcomp.sty)
Provides:       tex(icsv.cls) = %{tl_version}

%description -n texlive-icsv
This is an ad-hoc class for typesetting articles for the ICSV
conference, based on the earler active-conf by the same author.

%package -n texlive-icsv-doc
Summary:        Documentation for icsv
Version:        svn15878.0.2

Provides:       tex-icsv-doc
AutoReqProv:    No

%description -n texlive-icsv-doc
Documentation for icsv

%package -n texlive-ieeepes
Provides:       tex-ieeepes = %{tl_version}
License:        LPPL
Summary:        IEEE Power Engineering Society Transactions
Version:        svn17359.4.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(vmargin.sty), tex(graphicx.sty), tex(times.sty), tex(mathptm.sty)
Provides:       tex(ieeepes.sty) = %{tl_version}

%description -n texlive-ieeepes
Supports typesetting of transactions, as well as discussions
and closures, for the IEEE Power Engineering Society
Transactions journals.

%package -n texlive-ieeepes-doc
Summary:        Documentation for ieeepes
Version:        svn17359.4.0

Provides:       tex-ieeepes-doc
AutoReqProv:    No

%description -n texlive-ieeepes-doc
Documentation for ieeepes

%package -n texlive-ijmart
Provides:       tex-ijmart = %{tl_version}
License:        LPPL
Summary:        LaTeX Class for the Israel Journal of Mathematics
Version:        svn30958.1.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(fancyhdr.sty), tex(lastpage.sty)
Provides:       tex(ijmart.cls) = %{tl_version}

%description -n texlive-ijmart
The Israel Journal of Mathematics is published by The Hebrew
University Magnes Press. This class provides LaTeX support for
its authors and editors. It strives to achieve the distinct
"look and feel" of the journal, while having the interface
similar to that of the amsart document class. This will help
authors already familiar with amsart to easily submit
manuscripts for The Israel Journal of Mathematics or to put the
preprints in arXiv with minimal changes in the LaTeX source.

%package -n texlive-ijmart-doc
Summary:        Documentation for ijmart
Version:        svn30958.1.7

Provides:       tex-ijmart-doc
AutoReqProv:    No

%description -n texlive-ijmart-doc
Documentation for ijmart

%package -n texlive-imac
Provides:       tex-imac = %{tl_version}
License:        GPL+
Summary:        International Modal Analysis Conference format
Version:        svn17347.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(imac.sty) = %{tl_version}

%description -n texlive-imac
A set of files for producing correctly formatted documents for
the International Modal Analysis Conference. The bundle
provides a LaTeX package and a BibTeX style file.

%package -n texlive-imac-doc
Summary:        Documentation for imac
Version:        svn17347.0

Provides:       tex-imac-doc
AutoReqProv:    No

%description -n texlive-imac-doc
Documentation for imac

%package -n texlive-imtekda
Provides:       tex-imtekda = %{tl_version}
License:        LPPL
Summary:        IMTEK thesis class
Version:        svn17667.1.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(calc.sty), tex(textpos.sty)
Provides:       tex(IMTEKda.cls) = %{tl_version}

%description -n texlive-imtekda
The class permits typesetting of diploma, bachelor's and
master's theses for the Institute of Microsystem Technology
(IMTEK) at the University of Freiburg (Germany). The class is
based on the KOMA-Script class scrbook. Included in the
documentation is a large collection of useful tips for
typesetting theses and a list of recommended packages.

%package -n texlive-imtekda-doc
Summary:        Documentation for imtekda
Version:        svn17667.1.7

Provides:       tex-imtekda-doc
AutoReqProv:    No

%description -n texlive-imtekda-doc
Documentation for imtekda

%package -n texlive-interchar
Provides:       tex-interchar = %{tl_version}
License:        LPPL 1.3
Summary:        Managing character class schemes in XeTeX
Version:        svn36312.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(xparse.sty)
Provides:       tex(interchar.sty) = %{tl_version}

%description -n texlive-interchar
The package manages character class schemes of XeTeX. Using
this package, you may switch among different character class
schemes. Migration commands are provided for make packages
using this mechanism compatible with each others.

%package -n texlive-interchar-doc
Summary:        Documentation for interchar
Version:        svn36312.0.2

Provides:       tex-interchar-doc
AutoReqProv:    No

%description -n texlive-interchar-doc
Documentation for interchar

%package -n texlive-hyphen-bulgarian-doc
Provides:       tex-hyphen-bulgarian-doc = %{tl_version}
License:        LPPL
Summary:        doc files of hyphen-bulgarian
Version:        svn48290
AutoReqProv:    No

%description -n texlive-hyphen-bulgarian-doc
Documentation for hyphen-bulgarian

%package -n texlive-hyphen-churchslavonic
Provides:       tex-hyphen-churchslavonic = %{tl_version}
License:        Copyright only
Summary:        Church Slavonic hyphenation patterns.
Version:        svn44401
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(hyph-cu.tex) = %{tl_version}, tex(loadhyph-cu.tex) = %{tl_version}

%description -n texlive-hyphen-churchslavonic
Hyphenation patterns for Church Slavonic in UTF-8 encoding

%package -n texlive-hyphen-occitan
Provides:       tex-hyphen-occitan = %{tl_version}
License:        Copyright only
Summary:        Occitan hyphenation patterns.
Version:        svn40340

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(hyph-oc.ec.tex) = %{tl_version}, tex(hyph-oc.tex) = %{tl_version}
Provides:       tex(hyph-quote-oc.tex) = %{tl_version}, tex(loadhyph-oc.tex) = %{tl_version}

%description -n texlive-hyphen-occitan
Hyphenation patterns for Occitan in T1/EC and UTF-8 encodings.
They are supposed to be valid for all the Occitan variants
spoken and written in the wide area called 'Occitanie' by the
French. It ranges from the Val d'Aran within Catalunya, to the
South Western Italian Alps encompassing the southern half of
the French pentagon.

%package -n texlive-hyphen-sanskrit-doc
Provides:       tex-hyphen-sanskrit-doc = %{tl_version}
License:        LPPL
Summary:        doc files of hyphen-sanskrit
Version:        svn40340

AutoReqProv:    No

%description -n texlive-hyphen-sanskrit-doc
Documentation for hyphen-sanskrit

%package -n texlive-hyphen-spanish-doc
Provides:       tex-hyphen-spanish-doc = %{tl_version}
License:        LPPL
Summary:        doc files of hyphen-spanish
Version:        svn40340

AutoReqProv:    No

%description -n texlive-hyphen-spanish-doc
Documentation for hyphen-spanish

%package -n texlive-ietfbibs-doc
Provides:       tex-ietfbibs-doc = %{tl_version}
License:        MIT
Summary:        doc files of ietfbibs
Version:        svn41332

AutoReqProv:    No

%description -n texlive-ietfbibs-doc
Documentation for ietfbibs

%package -n texlive-iffont-doc
Provides:       tex-iffont-doc = %{tl_version}
License:        LPPL
Summary:        doc files of iffont
Version:        svn38823

AutoReqProv:    No

%description -n texlive-iffont-doc
Documentation for iffont

%package -n texlive-iffont
Provides:       tex-iffont = %{tl_version}
License:        LPPL
Summary:        Conditionally load fonts with fontspec
Version:        svn38823

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(iffont.sty) = %{tl_version}

%description -n texlive-iffont
This package provides a macro to select the first font XeLaTeX
or LuaTeX can find in a comma separated list and, additionally,
a number of macro tests.

%package -n texlive-imfellenglish-doc
Provides:       tex-imfellenglish-doc = %{tl_version}
License:        LPPL and OFL
Summary:        doc files of imfellenglish
Version:        svn38547

AutoReqProv:    No

%description -n texlive-imfellenglish-doc
Documentation for imfellenglish

%package -n texlive-imfellenglish
Provides:       tex-imfellenglish = %{tl_version}
License:        LPPL and OFL
Summary:        IM Fell English fonts with LaTeX support
Version:        svn38547

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(imfellEnglish.sty) = %{tl_version}, tex(imfellEnglish.map) = %{tl_version}
Provides:       tex(TS1IMFELLEnglish-TLF.fd) = %{tl_version}
Provides:       tex(T1IMFELLEnglish-TLF.fd) = %{tl_version}
Provides:       tex(OT1IMFELLEnglish-TLF.fd) = %{tl_version}
Provides:       tex(LY1IMFELLEnglish-TLF.fd) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman.pfb) = %{tl_version}
Provides:       tex(IM_FELL_English_RomanLCDFJ.pfb) = %{tl_version}
Provides:       tex(IM_FELL_English_SC.pfb) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic.pfb) = %{tl_version}
Provides:       tex(IM_FELL_English_ItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(imfe_cycd4j.enc) = %{tl_version}, tex(imfe_fhc46f.enc) = %{tl_version}
Provides:       tex(imfe_s6atnx.enc) = %{tl_version}, tex(imfe_zxj6gt.enc) = %{tl_version}
Provides:       tex(imfe_5cupvv.enc) = %{tl_version}, tex(imfe_wnjo6u.enc) = %{tl_version}
Provides:       tex(imfe_dc7pev.enc) = %{tl_version}, tex(imfe_qauovj.enc) = %{tl_version}
Provides:       tex(imfe_uut767.enc) = %{tl_version}, tex(IMFeENsc28P.otf) = %{tl_version}
Provides:       tex(IMFeENit28P.otf) = %{tl_version}, tex(IMFeENrm28P.otf) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-t1.vf) = %{tl_version}
Provides:       tex(IM_FELL_English_SC-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IM_FELL_English_SC-tlf-t1.vf) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IM_FELL_English_SC-tlf-ot1.vf) = %{tl_version}
Provides:       tex(IM_FELL_English_SC-tlf-ts1.vf) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-ot1.vf) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(IM_FELL_English_SC-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_SC-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_SC-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_SC-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_SC-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_SC-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_SC-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_SC-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(IM_FELL_English_Roman-tlf-ot1.tfm) = %{tl_version}

%description -n texlive-imfellenglish
Igino Marini has implemented digital revivals of fonts
bequeathed to Oxford University by Dr. John Fell, Bishop of
Oxford and Dean of Christ Church in 1686. This package provides
the English family, consisting of Roman, Italic and Small-Cap
fonts.

%package -n texlive-hyphen-belarusian
Summary:        Belarusian hyphenation patterns.
Version:        svn44401
License:        Copyright only
Requires:       texlive-base texlive-kpathsea, texlive-hyphen-base
Requires:       texlive-hyph-utf8
Provides:       tex(loadhyph-be.tex) = %{tl_version}, tex(hyph-be.t2a.tex) = %{tl_version}
Provides:       tex(hyph-quote-be.tex) = %{tl_version}, tex(hyph-be.tex) = %{tl_version}

%description -n texlive-hyphen-belarusian
Belarusian hyphenation patterns in T2A and UTF-8 encodings

%post -n texlive-hyphen-belarusian
if [ $1 -gt 0 ] ; then
sed -i '/belarusian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat
echo "belarusian loadhyph-be.tex" >> %{_texdir}/texmf-dist/tex/generic/config/language.dat
sed -i '/\\addlanguage{belarusian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def
echo "\addlanguage{belarusian}{loadhyph-be.tex}{}{2}{2}" >> %{_texdir}/texmf-dist/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-belarusian
if [ $1 == 0 ] ; then
sed -i '/belarusian.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.dat > /dev/null 2>&1
sed -i '/\\addlanguage{belarusian}.*/d' %{_texdir}/texmf-dist/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%package -n texlive-ifptex
Summary:        Check if the engine is pTeX or one of its derivatives
Version:        svn45485
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ifptex.sty) = %{tl_version}, tex(ifuptex.sty) = %{tl_version}

%description -n texlive-ifptex
The ifptex package is a counterpart of ifxetex, ifluatex, etc.
for the ptex engine. The ifuptex package is an alias to ifptex
provided for backward compatibility.

%package -n texlive-ifxptex
Summary:        Detect pTeX and its derivatives
Version:        svn46153
License:        Knuth
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ifxptex.sty) = %{tl_version}

%description -n texlive-ifxptex
The package provides commands for detecting pTeX and its
derivatives (e-pTeX, upTeX, e-upTeX, and ApTeX). Both LaTeX and
plain TeX are supported.

%package -n texlive-ijsra
Summary:        LaTeX document class for the International Journal of Student Research in Archaeology
Version:        svn44886
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ijsra.cls) = %{tl_version}

%description -n texlive-ijsra
This is a document class called ijsra which is used for the
International Journal of Student Research in Archaeology.

%package -n texlive-invoice2
Summary:        Intelligent invoices with LaTeX3
Version:        svn46364
License:        GPLv3+
Requires:       texlive-base texlive-kpathsea
Provides:       tex(invoice2.sty) = %{tl_version}

%description -n texlive-invoice2
Typeset invoices with automatic VAT and calculation of totals.
Supports internationalization, invoices are typeset with
booktabs for readability. Does not support separate projects
per invoice. Can be used as a replacement for invoice in most
cases.

%package -n texlive-hyperbar
Summary:        Add interactive Barcode fields to PDF forms
Version:        svn48147
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(hyperbar.sty) = %{tl_version}

%description -n texlive-hyperbar
The package extends the hyperref functionality for creating
interactive forms to allow adding Barcode form fields supported
by some modern PDF readers. Currently, only pdfTeX is
supported.

%package -n texlive-includernw
Summary:        Include .Rnw inside .tex
Version:        svn47557
License:        LPPL
Requires:       texlive-base texlive-kpathsea, R-knitr
Provides:       tex(includeRnw.sty) = %{tl_version}

%description -n texlive-includernw
This package is for including .Rnw (knitr/sweave)-files inside
.tex-files. It requires that you have R and the R-package knitr
installed.

%package -n texlive-intopdf
Summary:        Embed non-PDF files into PDF with hyperlink
Version:        svn46988
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(intopdf.sty) = %{tl_version}

%description -n texlive-intopdf
The package allows to embed non-PDF files (e.g., BibTeX) into
PDF with a hyperlink.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/inconsolata"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir

install %{buildroot}%{_texdir}/texmf-dist/tex/generic/config/language.us %{buildroot}%{_texdir}/texmf-dist/tex/generic/config/language.dat
install %{buildroot}%{_texdir}/texmf-dist/tex/generic/config/language.us.def %{buildroot}%{_texdir}/texmf-dist/tex/generic/config/language.def

install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*
install -d %{buildroot}%{_sysconfdir}/texlive/tex/generic/config
mv %{buildroot}%{_texdir}/texmf-dist/tex/generic/config/language.dat %{buildroot}%{_sysconfdir}/texlive/tex/generic/config/
ln -s %{_sysconfdir}/texlive/tex/generic/config/language.dat %{buildroot}%{_texdir}/texmf-dist/tex/generic/config/language.dat

%files -n texlive-hyph-utf8
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-il2.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-il3.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-l7x.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-lmc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-lth.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-qx.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-t8m.tex
%{_texdir}/texmf-dist/tex/luatex/hyph-utf8/etex.src
%{_texdir}/texmf-dist/tex/luatex/hyph-utf8/luatex-hyphen.lua

%files -n texlive-hyph-utf8-doc
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/
%{_texdir}/texmf-dist/doc/luatex/hyph-utf8/

%files -n texlive-hyphen-base
%{_texdir}/texmf-dist/tex/generic/hyphen/dumyhyph.tex
%{_texdir}/texmf-dist/tex/generic/hyphen/hyphen.tex
%{_texdir}/texmf-dist/tex/generic/hyphen/hypht1.tex
%{_texdir}/texmf-dist/tex/generic/hyphen/zerohyph.tex
%config(noreplace) %{_sysconfdir}/texlive/tex/generic/config/language.dat
%{_texdir}/texmf-dist/tex/generic/config/language.dat
%{_texdir}/texmf-dist/tex/generic/config/language.dat.lua
%{_texdir}/texmf-dist/tex/generic/config/language.def
%{_texdir}/texmf-dist/tex/generic/config/language.us
%{_texdir}/texmf-dist/tex/generic/config/language.us.def
%{_texdir}/texmf-dist/tex/generic/config/language.us.lua

%files -n texlive-ifluatex
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/oberdiek/ifluatex.sty

%files -n texlive-ifluatex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/oberdiek/ifluatex.pdf
%{_texdir}/texmf-dist/doc/latex/oberdiek/test/ifluatex-test1.tex
%{_texdir}/texmf-dist/doc/latex/oberdiek/test/ifluatex-test2.tex
%{_texdir}/texmf-dist/doc/latex/oberdiek/test/ifluatex-test3.tex

%files -n texlive-ifxetex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/ifxetex/

%files -n texlive-ifxetex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/ifxetex/

%files -n texlive-hyperref
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hyperref/

%files -n texlive-hyperref-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hyperref/

%files -n texlive-ijqc
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/ijqc/

%files -n texlive-ijqc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/bibtex/ijqc/

%files -n texlive-inlinebib
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/inlinebib/
%{_texdir}/texmf-dist/tex/latex/inlinebib/

%files -n texlive-inlinebib-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/bibtex/inlinebib/

%files -n texlive-iopart-num
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/iopart-num/

%files -n texlive-iopart-num-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/bibtex/iopart-num/

%files -n texlive-hyphenex
%{_texdir}/texmf-dist/tex/generic/hyphenex/

%files -n texlive-ifsym
%{_texdir}/texmf-dist/fonts/source/public/ifsym/
%{_texdir}/texmf-dist/fonts/tfm/public/ifsym/
%{_texdir}/texmf-dist/tex/latex/ifsym/

%files -n texlive-ifsym-doc
%{_texdir}/texmf-dist/doc/fonts/ifsym/

%files -n texlive-inconsolata
%{_datadir}/fonts/inconsolata
%{_texdir}/texmf-dist/fonts/enc/dvips/inconsolata/
%{_texdir}/texmf-dist/fonts/map/dvips/inconsolata/
%{_texdir}/texmf-dist/fonts/opentype/public/inconsolata/
%{_texdir}/texmf-dist/fonts/tfm/public/inconsolata/
%{_texdir}/texmf-dist/fonts/type1/public/inconsolata/
%{_texdir}/texmf-dist/tex/latex/inconsolata/

%files -n texlive-inconsolata-doc
%{_texdir}/texmf-dist/doc/fonts/inconsolata/

%files -n texlive-initials
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/initials/
%{_texdir}/texmf-dist/fonts/afm/public/initials/
%{_texdir}/texmf-dist/fonts/map/dvips/initials/
%{_texdir}/texmf-dist/fonts/tfm/public/initials/
%{_texdir}/texmf-dist/fonts/type1/public/initials/
%{_texdir}/texmf-dist/tex/latex/initials/

%files -n texlive-initials-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/initials/

%files -n texlive-ipaex-type1
%license other-free.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/ipaex-type1/
%{_texdir}/texmf-dist/fonts/map/dvips/ipaex-type1/
%{_texdir}/texmf-dist/fonts/tfm/public/ipaex-type1/
%{_texdir}/texmf-dist/fonts/type1/public/ipaex-type1/
%{_texdir}/texmf-dist/tex/latex/ipaex-type1/

%files -n texlive-ipaex-type1-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/fonts/ipaex-type1/

%files -n texlive-ifetex
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ifetex/
%{_texdir}/texmf-dist/tex/plain/ifetex/

%files -n texlive-ifetex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ifetex/

%files -n texlive-iftex
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/iftex/

%files -n texlive-iftex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/iftex/

%files -n texlive-insbox
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/insbox/

%files -n texlive-insbox-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/generic/insbox/

%files -n texlive-hyphen-ethiopic
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-mul-ethi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-mul-ethi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.pat.txt

%files -n texlive-hyphen-arabic

%files -n texlive-hyphen-farsi

%files -n texlive-imsproc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/imsproc/

%files -n texlive-imsproc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/imsproc/

%files -n texlive-hyphen-chinese
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-zh-latn-pinyin.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-zh-latn-pinyin.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-zh-latn-pinyin.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-zh-latn-pinyin.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.pat.txt

%files -n texlive-impatient-cn-doc
%{_texdir}/texmf-dist/doc/plain/impatient-cn/

%files -n texlive-hyphen-bulgarian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-bg.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-bg.t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-bg.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bg.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bg.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bg.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bg.pat.txt

%files -n texlive-hyphen-mongolian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-mn-cyrl-x-lmc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-mn-cyrl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-mn-cyrl-x-lmc.lmc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-mn-cyrl.t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-mn-cyrl-x-lmc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-mn-cyrl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.pat.txt

%files -n texlive-hyphen-russian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ru.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-ru.t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ru.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ru.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ru.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ru.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ru.pat.txt

%files -n texlive-hyphen-serbian
%license gpl.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-sr-cyrl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-sr-latn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-sh-cyrl.t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-sh-latn.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sh-cyrl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sh-latn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sr-cyrl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.pat.txt

%files -n texlive-hyphen-ukrainian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-uk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-uk.t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-uk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-uk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-uk.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-uk.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-uk.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-uk.pat.txt


%files -n texlive-hyphen-czech
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-cs.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-cs.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-cs.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cs.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cs.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cs.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cs.pat.txt

%files -n texlive-hyphen-slovak
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-sk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-sk.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sk.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sk.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sk.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sk.pat.txt

%files -n texlive-hyphen-english
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-en-gb.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-en-us.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-en-gb.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-en-us.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.pat.txt

%files -n texlive-impatient-doc
%license fdl.txt
%{_texdir}/texmf-dist/doc/plain/impatient/

%files -n texlive-intro-scientific-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/intro-scientific/

%files -n texlive-hyphen-armenian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-hy.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-hy.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hy.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hy.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hy.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hy.pat.txt

%files -n texlive-hyphen-croatian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-hr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-hr.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-hr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hr.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hr.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hr.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hr.pat.txt

%files -n texlive-hyphen-danish
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-da.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-da.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-da.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-da.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-da.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-da.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-da.pat.txt

%files -n texlive-hyphen-dutch
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-nl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-nl.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-nl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nl.pat.txt

%files -n texlive-hyphen-estonian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-et.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-et.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-et.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-et.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-et.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-et.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-et.pat.txt

%files -n texlive-hyphen-finnish
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-fi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-fi.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-fi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fi.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fi.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fi.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fi.pat.txt

%files -n texlive-hyphen-friulan
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-fur.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-fur.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-fur.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-fur.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fur.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fur.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fur.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fur.pat.txt

%files -n texlive-hyphen-hungarian
%license gpl.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-hu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-hu.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-hu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hu.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hu.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hu.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hu.pat.txt

%files -n texlive-hyphen-hungarian-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/generic/huhyphen/

%files -n texlive-hyphen-icelandic
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-is.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-is.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-is.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-is.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-is.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-is.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-is.pat.txt

%files -n texlive-hyphen-irish
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ga.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-ga.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ga.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ga.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ga.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ga.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ga.pat.txt

%files -n texlive-hyphen-kurmanji
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-kmr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-kmr.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-kmr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.pat.txt

%files -n texlive-hyphen-latin
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-la-x-classic.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-la-x-liturgic.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-la.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-la-x-liturgic.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-la.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-la-x-classic.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-la-x-liturgic.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-la.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la-x-classic.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la-x-classic.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la-x-classic.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la-x-classic.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la-x-liturgic.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la-x-liturgic.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la-x-liturgic.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la-x-liturgic.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la.pat.txt

%files -n texlive-hyphen-latvian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-lv.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-lv.l7x.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-lv.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lv.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lv.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lv.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lv.pat.txt

%files -n texlive-hyphen-lithuanian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-lt.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-lt.l7x.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-lt.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lt.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lt.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lt.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lt.pat.txt

%files -n texlive-hyphen-norwegian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-nb.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-nn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-nb.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-nn.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-nb.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-nn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-no.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nb.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nb.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nb.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nb.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nn.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nn.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nn.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nn.pat.txt

%files -n texlive-hyphen-piedmontese
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-pms.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-pms.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-pms.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pms.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pms.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pms.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pms.pat.txt

%files -n texlive-hyphen-romanian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ro.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-ro.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ro.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ro.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ro.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ro.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ro.pat.txt

%files -n texlive-hyphen-romansh
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-rm.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-rm.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-rm.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-rm.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-rm.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-rm.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-rm.pat.txt

%files -n texlive-hyphen-slovenian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-sl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-sl.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sl.pat.txt

%files -n texlive-hyphen-swedish
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-sv.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-sv.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sv.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sv.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sv.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sv.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sv.pat.txt

%files -n texlive-hyphen-turkish
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-tr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-tr.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-tr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tr.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tr.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tr.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tr.pat.txt

%files -n texlive-hyphen-uppersorbian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-hsb.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-hsb.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-hsb.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.pat.txt

%files -n texlive-hyphen-welsh
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-cy.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-cy.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-cy.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cy.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cy.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cy.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cy.pat.txt

%files -n texlive-hyphen-basque
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-eu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-eu.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-eu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eu.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eu.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eu.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eu.pat.txt

%files -n texlive-hyphen-french
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-fr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-fr.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-fr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-fr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fr.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fr.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fr.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fr.pat.txt

%files -n texlive-impatient-fr-doc
%license fdl.txt
%{_texdir}/texmf-dist/doc/plain/impatient-fr/

%files -n texlive-impnattypo
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/impnattypo/

%files -n texlive-impnattypo-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/impnattypo/

%files -n texlive-hyphen-german
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-de-1901.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-de-1996.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-de-ch-1901.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-de-1901.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-de-1996.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-de-ch-1901.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-de-1901.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-de-1996.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-de-ch-1901.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyphen/dehyphn.tex
%{_texdir}/texmf-dist/tex/generic/hyphen/dehypht.tex
%{_texdir}/texmf-dist/tex/generic/hyphen/dehyphtex.tex
%{_texdir}/texmf-dist/tex/generic/hyphen/ghyphen.README

%files -n texlive-hyphen-greek
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-el-monoton.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-el-polyton.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-el-monoton.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-el-polyton.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyphen/grmhyph5.tex
%{_texdir}/texmf-dist/tex/generic/hyphen/grphyph5.tex

%files -n texlive-hyphen-greek-doc
%{_texdir}/texmf-dist/doc/generic/elhyphen/

%files -n texlive-hyphen-ancientgreek
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-grc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-grc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-grc.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-grc.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-grc.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-grc.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyphen/grahyph5.tex
%{_texdir}/texmf-dist/tex/generic/hyphen/ibyhyph.tex

%files -n texlive-ibycus-babel
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ibycus-babel/

%files -n texlive-ibycus-babel-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ibycus-babel/

%files -n texlive-ibygrk
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/ibygrk/
%{_texdir}/texmf-dist/fonts/enc/dvips/ibygrk/
%{_texdir}/texmf-dist/fonts/map/dvips/ibygrk/
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/
%{_texdir}/texmf-dist/fonts/tfm/public/ibygrk/
%{_texdir}/texmf-dist/fonts/type1/public/ibygrk/
%{_texdir}/texmf-dist/tex/generic/ibygrk/

%files -n texlive-ibygrk-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/ibygrk/

%files -n texlive-hyphen-indic
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-as.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-bn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-gu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-hi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-kn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ml.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-mr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-or.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-pa.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-pi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ta.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-te.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-as.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-bn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-gu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-hi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-kn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ml.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-mr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-or.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-pa.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-pi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ta.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-te.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-as.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-as.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-as.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-as.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bn.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bn.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bn.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bn.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gu.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gu.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gu.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gu.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hi.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hi.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hi.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hi.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kn.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kn.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kn.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kn.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ml.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ml.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ml.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ml.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mr.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mr.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mr.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mr.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-or.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-or.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-or.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-or.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pa.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pa.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pa.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pa.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pi.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pi.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pi.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pi.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ta.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ta.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ta.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ta.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-te.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-te.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-te.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-te.pat.txt

%files -n texlive-hyphen-sanskrit
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-sa.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sa.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sa.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sa.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sa.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sa.pat.txt

%files -n texlive-hyphen-italian
%license lgpl2.1.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-it.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-it.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-it.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-it.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-it.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-it.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-it.pat.txt

%files -n texlive-ipaex
%{_texdir}/texmf-dist/fonts/truetype/public/ipaex/

%files -n texlive-ipaex-doc
%{_texdir}/texmf-dist/doc/fonts/ipaex/

%files -n texlive-hyphen-afrikaans
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-af.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-af.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-af.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-af.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-af.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-af.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-af.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-af.pat.txt

%files -n texlive-hyphen-coptic
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-cop.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex-8bit/copthyph.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-cop.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cop.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cop.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cop.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cop.pat.txt

%files -n texlive-hyphen-esperanto
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-eo.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-eo.il3.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-eo.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eo.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eo.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eo.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eo.pat.txt

%files -n texlive-hyphen-georgian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ka.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-ka.t8m.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ka.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ka.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ka.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ka.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ka.pat.txt

%files -n texlive-hyphen-indonesian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-id.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-id.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-id.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-id.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-id.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-id.pat.txt

%files -n texlive-hyphen-interlingua
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ia.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ia.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ia.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ia.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ia.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ia.pat.txt

%files -n texlive-hyphen-thai
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-th.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-th.lth.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-th.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-th.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-th.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-th.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-th.pat.txt

%files -n texlive-hyphen-turkmen
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-tk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-tk.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-tk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tk.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tk.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tk.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tk.pat.txt

%files -n texlive-hyphen-polish
%license knuth.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-pl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-pl.qx.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-pl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pl.pat.txt

%files -n texlive-hyphen-portuguese
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-pt.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-pt.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-pt.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pt.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pt.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pt.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pt.pat.txt

%files -n texlive-hyphen-catalan
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ca.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-ca.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ca.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ca.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ca.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ca.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ca.pat.txt

%files -n texlive-hyphen-galician
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-gl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-gl.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-gl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gl.pat.txt

%files -n texlive-hyphen-spanish
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-es.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-es.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-es.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-es.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-es.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-es.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-es.pat.txt

%files -n texlive-index
%{_texdir}/texmf-dist/bibtex/bst/index/
%{_texdir}/texmf-dist/makeindex/index/
%{_texdir}/texmf-dist/tex/latex/index/

%files -n texlive-index-doc
%{_texdir}/texmf-dist/doc/latex/index/

%files -n texlive-ifmtarg
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ifmtarg/

%files -n texlive-ifmtarg-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ifmtarg/

%files -n texlive-hypdvips
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/hypdvips/

%files -n texlive-hypdvips-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/hypdvips/

%files -n texlive-hyper
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hyper/

%files -n texlive-hyper-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hyper/

%files -n texlive-hypernat
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/hypernat/

%files -n texlive-hypernat-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/hypernat/

%files -n texlive-hyperxmp
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/hyperxmp/

%files -n texlive-hyperxmp-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/hyperxmp/

%files -n texlive-hyphenat
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/hyphenat/

%files -n texlive-hyphenat-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/hyphenat/

%files -n texlive-idxcmds
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/idxcmds/

%files -n texlive-idxcmds-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/idxcmds/

%files -n texlive-idxlayout
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/idxlayout/

%files -n texlive-idxlayout-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/idxlayout/

%files -n texlive-ifmslide
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/ifmslide/

%files -n texlive-ifmslide-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/ifmslide/

%files -n texlive-ifnextok
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ifnextok/

%files -n texlive-ifnextok-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ifnextok/

%files -n texlive-ifoddpage
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ifoddpage/

%files -n texlive-ifoddpage-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ifoddpage/

%files -n texlive-ifplatform
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ifplatform/

%files -n texlive-ifplatform-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ifplatform/

%files -n texlive-ifthenx
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ifthenx/

%files -n texlive-ifthenx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ifthenx/

%files -n texlive-iitem
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/iitem/

%files -n texlive-iitem-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/iitem/

%files -n texlive-image-gallery
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/image-gallery/

%files -n texlive-image-gallery-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/image-gallery/

%files -n texlive-imakeidx
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/imakeidx/

%files -n texlive-imakeidx-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/imakeidx/

%files -n texlive-import
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/import/

%files -n texlive-import-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/import/

%files -n texlive-incgraph
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/incgraph/

%files -n texlive-incgraph-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/incgraph/

%files -n texlive-indextools
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/indextools/

%files -n texlive-indextools-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/indextools/

%files -n texlive-inlinedef
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/inlinedef/

%files -n texlive-inlinedef-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/inlinedef/

%files -n texlive-inputtrc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/inputtrc/

%files -n texlive-inputtrc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/inputtrc/

%files -n texlive-interactiveworkbook
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/interactiveworkbook/

%files -n texlive-interactiveworkbook-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/

%files -n texlive-interfaces
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/interfaces/

%files -n texlive-interfaces-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/interfaces/

%files -n texlive-inversepath
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/inversepath/

%files -n texlive-inversepath-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/inversepath/

%files -n texlive-invoice
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/invoice/

%files -n texlive-invoice-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/invoice/

%files -n texlive-interpreter
%license lppl1.txt
%{_texdir}/texmf-dist/tex/luatex/interpreter/

%files -n texlive-interpreter-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/luatex/interpreter/

%files -n texlive-interval
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/interval/

%files -n texlive-interval-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/interval/

%files -n texlive-ionumbers
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/ionumbers/

%files -n texlive-ionumbers-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/ionumbers/

%files -n texlive-hyplain
%license pd.txt
%{_texdir}/texmf-dist/tex/plain/hyplain/

%files -n texlive-hyplain-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/plain/hyplain/

%files -n texlive-icsv
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/icsv/

%files -n texlive-icsv-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/icsv/

%files -n texlive-ieeepes
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/ieeepes/
%{_texdir}/texmf-dist/tex/latex/ieeepes/

%files -n texlive-ieeepes-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ieeepes/

%files -n texlive-ijmart
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/ijmart/
%{_texdir}/texmf-dist/tex/latex/ijmart/

%files -n texlive-ijmart-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ijmart/

%files -n texlive-imac
%license gpl.txt
%{_texdir}/texmf-dist/bibtex/bst/imac/
%{_texdir}/texmf-dist/tex/latex/imac/

%files -n texlive-imac-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/imac/

%files -n texlive-imtekda
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/imtekda/

%files -n texlive-imtekda-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/imtekda/

%files -n texlive-interchar
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/interchar/

%files -n texlive-interchar-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/interchar/

%files -n texlive-hyphen-bulgarian-doc
%license lppl.txt
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/bg/azbukaExtended.pdf
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/bg/azbukaExtended.tex

%files -n texlive-hyphen-churchslavonic
%license other-free.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cu.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cu.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cu.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cu.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-cu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-cu.tex

%files -n texlive-hyphen-occitan
%license other-free.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-oc.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-oc.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-oc.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-oc.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-oc.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-oc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-oc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-oc.tex

%files -n texlive-hyphen-sanskrit-doc
%license lppl.txt
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/sa/hyphenmin.txt

%files -n texlive-hyphen-spanish-doc
%license lppl.txt
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/es/README
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/es/division.pdf

%files -n texlive-ietfbibs-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/bibtex/ietfbibs/

%files -n texlive-iffont-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/iffont/

%files -n texlive-iffont
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/iffont/

%files -n texlive-imfellenglish-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/imfellenglish/

%files -n texlive-imfellenglish
%license ofl.txt
%{_texdir}/texmf-dist/tex/latex/imfellenglish/
%{_texdir}/texmf-dist/fonts/opentype/iginomarini/imfellenglish/
%{_texdir}/texmf-dist/fonts/map/dvips/imfellenglish/
%{_texdir}/texmf-dist/fonts/tfm/iginomarini/imfellenglish/
%{_texdir}/texmf-dist/fonts/vf/iginomarini/imfellenglish/
%{_texdir}/texmf-dist/fonts/enc/dvips/imfellenglish/
%{_texdir}/texmf-dist/fonts/type1/iginomarini/imfellenglish/

%files -n texlive-hyphen-belarusian
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-be.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-be.t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-be.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-be.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-be.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-be.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-be.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-be.pat.txt

%files -n texlive-ifptex
%doc %{_texdir}/texmf-dist/doc/generic/ifptex/
%{_texdir}/texmf-dist/tex/generic/ifptex/

%files -n texlive-ifxptex
%license knuth.txt
%doc %{_texdir}/texmf-dist/doc/generic/ifxptex/
%{_texdir}/texmf-dist/tex/generic/ifxptex/

%files -n texlive-ijsra
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/ijsra/
%{_texdir}/texmf-dist/tex/latex/ijsra/

%files -n texlive-invoice2
%license gpl3.txt
%doc %{_texdir}/texmf-dist/doc/latex/invoice2/
%{_texdir}/texmf-dist/tex/latex/invoice2/

%files -n texlive-hyperbar
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/hyperbar/
%doc %{_texdir}/texmf-dist/doc/latex/hyperbar/

%files -n texlive-includernw
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/includernw/
%doc %{_texdir}/texmf-dist/doc/latex/includernw/

%files -n texlive-intopdf
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/intopdf/
%doc %{_texdir}/texmf-dist/doc/latex/intopdf/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
