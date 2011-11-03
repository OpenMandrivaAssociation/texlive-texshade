# revision 23795
# category Package
# catalog-ctan /macros/latex/contrib/texshade
# catalog-date 2011-06-02 21:02:40 +0200
# catalog-license gpl2
# catalog-version 1.23
Name:		texlive-texshade
Version:	1.23
Release:	1
Summary:	Package for setting nucleotide and peptide alignments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texshade
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texshade.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texshade.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texshade.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
