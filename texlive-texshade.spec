Name:		texlive-texshade
Version:	64242
Release:	1
Summary:	Package for setting nucleotide and peptide alignments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texshade
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texshade.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texshade.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texshade.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/texshade
%doc %{_texmfdistdir}/doc/latex/texshade
#- source
%doc %{_texmfdistdir}/source/latex/texshade

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
