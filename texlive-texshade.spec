# revision 24716
# category Package
# catalog-ctan /macros/latex/contrib/texshade
# catalog-date 2011-12-01 13:24:33 +0100
# catalog-license gpl2
# catalog-version 1.24
Name:		texlive-texshade
Version:	1.24
Release:	4
Summary:	Package for setting nucleotide and peptide alignments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texshade
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texshade.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texshade.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texshade.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXshade is alignment shading software completely written in
TeX/LaTeX; it can process multiple sequence alignments in the
.MSF and the .ALN file formats. In addition to common shading
algorithms, it provides special shading modes showing
functional aspects, e.g. charge or hydropathy, and a wide range
of commands for handling shading colours, text styles, labels,
legends; it even allows the user to define completely new
shading modes. TeXshade combines highest flexibility with TeX
output quality -- all in a bundle that does not demand
excessive development time of the user.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/texshade/texshade.def
%{_texmfdistdir}/tex/latex/texshade/texshade.sty
%doc %{_texmfdistdir}/doc/latex/texshade/AQP1.phd
%doc %{_texmfdistdir}/doc/latex/texshade/AQP1.top
%doc %{_texmfdistdir}/doc/latex/texshade/AQP2spec.ALN
%doc %{_texmfdistdir}/doc/latex/texshade/AQPDNA.MSF
%doc %{_texmfdistdir}/doc/latex/texshade/AQP_HMM.ext
%doc %{_texmfdistdir}/doc/latex/texshade/AQP_HMM.sgl
%doc %{_texmfdistdir}/doc/latex/texshade/AQP_TC.asc
%doc %{_texmfdistdir}/doc/latex/texshade/AQPpro.MSF
%doc %{_texmfdistdir}/doc/latex/texshade/README
%doc %{_texmfdistdir}/doc/latex/texshade/ciliate.cod
%doc %{_texmfdistdir}/doc/latex/texshade/standard.cod
%doc %{_texmfdistdir}/doc/latex/texshade/texshade.pdf
%doc %{_texmfdistdir}/doc/latex/texshade/tsfaq.pdf
%doc %{_texmfdistdir}/doc/latex/texshade/tsfaq.tex
#- source
%doc %{_texmfdistdir}/source/latex/texshade/texshade.dtx
%doc %{_texmfdistdir}/source/latex/texshade/texshade.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
