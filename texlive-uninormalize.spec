Name:		texlive-uninormalize
Version:	57257
Release:	2
Summary:	Unicode normalization support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uninormalize
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uninormalize.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uninormalize.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides Unicode normalization (useful for
composed characters) for LuaLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/uninormalize
%doc %{_texmfdistdir}/doc/lualatex/uninormalize

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
